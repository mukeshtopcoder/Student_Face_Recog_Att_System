import streamlit as st
from src.ui import require_login
from src.authentication import hash_password
from src.database import execute

require_login()
st.header("Admin")
st.write("Create an administrator account. Passwords are stored as bcrypt hashes.")
with st.form("new_admin"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Create admin")
if submitted:
    if not username.strip() or len(password) < 8:
        st.error("Use a username and a password of at least 8 characters.")
    else:
        try:
            execute("INSERT INTO users (username,password_hash,role) VALUES (%s,%s,'admin')", (username.strip(), hash_password(password)))
            st.success("Admin account created.")
        except Exception as exc:
            st.error(f"Could not create admin: {exc}")
