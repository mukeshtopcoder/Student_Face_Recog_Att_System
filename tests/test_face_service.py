import numpy as np
from src.face_recognition_service import save_encoding, load_known_encodings

def test_encoding_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr("src.face_recognition_service.ENCODINGS_DIR", tmp_path)
    vector = np.array([0.1, 0.2, 0.3])
    path = save_encoding("S001", vector)
    assert path.endswith("S001.npy")
    assert np.allclose(load_known_encodings()["S001"], vector)
