from pathlib import Path
import numpy as np

ENCODINGS_DIR = Path("encodings")

def _library():
    try:
        import face_recognition
        return face_recognition
    except ImportError as exc:
        raise RuntimeError("Install face-recognition to use camera recognition.") from exc

def encode_image(image):
    face_recognition = _library()
    locations = face_recognition.face_locations(image)
    if len(locations) != 1:
        raise ValueError("Provide an image containing exactly one face.")
    encodings = face_recognition.face_encodings(image, locations)
    if not encodings:
        raise ValueError("A usable face encoding could not be generated.")
    return encodings[0]

def save_encoding(student_id, encoding):
    ENCODINGS_DIR.mkdir(exist_ok=True)
    path = ENCODINGS_DIR / f"{student_id}.npy"
    np.save(path, encoding)
    return str(path)

def load_known_encodings():
    ENCODINGS_DIR.mkdir(exist_ok=True)
    result = {}
    for path in ENCODINGS_DIR.glob("*.npy"):
        result[path.stem] = np.load(path)
    return result

def recognize(image, known_encodings, tolerance=0.48):
    face_recognition = _library()
    locations = face_recognition.face_locations(image)
    if len(locations) != 1:
        return None, "Detect exactly one face before marking attendance."
    encoding = face_recognition.face_encodings(image, locations)[0]
    if not known_encodings:
        return None, "No registered face encodings are available."
    ids = list(known_encodings)
    distances = face_recognition.face_distance([known_encodings[i] for i in ids], encoding)
    index = int(np.argmin(distances))
    distance = float(distances[index])
    return (ids[index], distance) if distance <= tolerance else (None, f"Unknown face (distance {distance:.3f}).")
