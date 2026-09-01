from datetime import date, timedelta
import io
import pandas as pd
import streamlit as st
from src.ui import require_login
from src.attendance_service import fetch_attendance
from src.student_service import list_students

require_login()
st.header("Attendance reports")
try:
    students = list_students()
    options = ["All students"] + [f"{s['student_id']} - {s['name']}" for s in students]
    selected = st.selectbox("Student", options)
    start = st.date_input("From", date.today() - timedelta(days=30))
    end = st.date_input("To", date.today())
    student_id = None if selected == "All students" else selected.split(" - ", 1)[0]
    rows = fetch_attendance(student_id, start, end)
    df = pd.DataFrame(rows)
    st.metric("Records", len(df))
    st.dataframe(df, use_container_width=True, hide_index=True)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "attendance_report.csv", "text/csv")
    excel = io.BytesIO()
    with pd.ExcelWriter(excel, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Attendance")
    st.download_button("Download Excel", excel.getvalue(), "attendance_report.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
except Exception as exc:
    st.error(f"Report data is unavailable: {exc}")
