import streamlit as st
import numpy as np
from src.ui import require_login
from src.attendance_service import mark_attendance
from src.face_recognition_service import recognize, load_known_encodings
from src.config import settings

require_login()
st.header("Mark attendance")
image = st.camera_input("Capture one face")
if image:
    try:
        import cv2
        raw = np.asarray(bytearray(image.getvalue()), dtype=np.uint8)
        rgb = cv2.cvtColor(cv2.imdecode(raw, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
        student_id, detail = recognize(rgb, load_known_encodings(), settings.face_tolerance)
        if student_id:
            st.success(f"Recognized student: {student_id} (distance {detail:.3f})")
            if st.button("Confirm and mark attendance", type="primary"):
                ok, message = mark_attendance(student_id)
                (st.success if ok else st.warning)(message)
        else:
            st.warning(detail)
    except Exception as exc:
        st.error(f"Recognition failed: {exc}")
