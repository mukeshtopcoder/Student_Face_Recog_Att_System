import streamlit as st
from src.ui import require_login
from src.student_service import dashboard_metrics

require_login()
st.header("Dashboard")
try:
    m = dashboard_metrics()
    cols = st.columns(4)
    cols[0].metric("Active students", m["students"])
    cols[1].metric("Present today", m["present"])
    cols[2].metric("Absent today", m["absent"])
    cols[3].metric("Attendance rate", f"{m['percentage']}%")
    st.subheader("Recent attendance")
    st.dataframe(m["recent"], use_container_width=True, hide_index=True)
except Exception as exc:
    st.error(f"Dashboard data is unavailable: {exc}")
