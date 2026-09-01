import streamlit as st

def require_login():
    if not st.session_state.get("user"):
        st.warning("Please sign in as an administrator from the home page.")
        st.stop()
