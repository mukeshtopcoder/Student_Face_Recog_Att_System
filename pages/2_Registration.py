import streamlit as st
import numpy as np
from src.ui import require_login
from src.student_service import create_student
from src.face_recognition_service import encode_image, save_encoding
from src.database import execute

require_login()
st.header("Student registration")
with st.form("registration"):
    student_id = st.text_input("Student ID", max_chars=20)
    name = st.text_input("Full name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    course = st.text_input("Course")
    image = st.camera_input("Capture a face image")
    submitted = st.form_submit_button("Register student", type="primary")

if submitted:
    if not student_id.strip() or not name.strip() or image is None:
        st.error("Student ID, name, and a face image are required.")
    else:
        try:
            frame = np.asarray(bytearray(image.getvalue()), dtype=np.uint8)
            import cv2
            rgb = cv2.cvtColor(cv2.imdecode(frame, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
            encoding = encode_image(rgb)
            create_student({"student_id": student_id.strip(), "name": name.strip(), "email": email.strip(), "phone": phone.strip(), "course": course.strip()})
            reference = save_encoding(student_id.strip(), encoding)
            execute("INSERT INTO face_encodings (student_id, encoding_reference) VALUES (%s,%s)", (student_id.strip(), reference))
            st.success("Student registered and face data saved.")
        except Exception as exc:
            st.error(f"Registration failed: {exc}")
