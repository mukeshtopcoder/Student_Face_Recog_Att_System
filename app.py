import streamlit as st
from src.authentication import authenticate
from src.database import health_check

st.set_page_config(page_title="CV Attendance", page_icon="📷", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

st.title("Intelligent Face Recognition Attendance")
st.caption("Computer vision attendance with auditable MySQL records")

if not st.session_state.user:
    st.subheader("Administrator sign in")
    with st.form("login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Sign in", type="primary")
    if submitted:
        try:
            user = authenticate(username.strip(), password)
            if user:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid username or password.")
        except Exception as exc:
            st.error(f"Unable to sign in: {exc}")
    st.info("Create the database and an admin user as described in README.md.")
else:
    st.sidebar.success(f"Signed in as {st.session_state.user['username']}")
    if st.sidebar.button("Sign out"):
        st.session_state.user = None
        st.rerun()
    ok, message = health_check()
    st.sidebar.caption(f"Database: {'online' if ok else 'offline'}")
    if not ok:
        st.warning("The database is unavailable. Configure .env and start MySQL before using the pages.")
    st.write("Use the pages in the sidebar to register students, mark attendance, manage records, and export reports.")
