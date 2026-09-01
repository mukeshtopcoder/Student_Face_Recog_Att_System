import streamlit as st
from src.ui import require_login
from src.student_service import list_students, set_active

require_login()
st.header("Student management")
try:
    students = list_students()
    search = st.text_input("Search by ID, name, or course")
    for student in students:
        haystack = " ".join(str(student.get(k, "")) for k in ("student_id", "name", "course")).lower()
        if search.lower() not in haystack:
            continue
        left, right = st.columns([5, 1])
        left.write(f"**{student['student_id']}** - {student['name']} · {student.get('course') or 'No course'} · {'Active' if student['is_active'] else 'Inactive'}")
        if right.button("Deactivate" if student["is_active"] else "Activate", key=student["student_id"]):
            set_active(student["student_id"], not student["is_active"])
            st.rerun()
except Exception as exc:
    st.error(f"Student records are unavailable: {exc}")
