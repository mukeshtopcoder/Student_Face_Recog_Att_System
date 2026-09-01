# Intelligent Face Recognition Attendance System

A modular student project built with Python, OpenCV, face recognition, MySQL, and Streamlit.

## Features

- Admin login with bcrypt password hashing
- Student registration and face-encoding storage on disk
- Camera-based recognition with configurable confidence threshold
- One attendance record per student per day, enforced in both code and MySQL
- Dashboard, student management, filtered reports, and CSV/Excel export
- Safe demo mode when MySQL/camera dependencies are not configured

## Quick start

1. Install Python 3.10+ and MySQL 8+.
2. Create an environment and install packages:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Create the database with `database/database.sql`.
4. Copy `.env.example` to `.env` and set the database credentials.
5. Create an admin password hash:

   ```powershell
   python -c "from src.authentication import hash_password; print(hash_password('change-me'))"
   ```

   Insert that hash into the `users` table.
6. Run the application:

   ```powershell
   streamlit run app.py
   ```

## Recognition notes

The default model is HOG for broad CPU compatibility. The system accepts a match only when the face distance is at most `FACE_TOLERANCE` (default `0.48`). Lower values reduce false positives but may reject more genuine matches. Recognition is not guaranteed; test under the lighting, pose, and camera conditions expected in deployment.

Face encodings are stored as `.npy` files under `encodings/`; raw images remain under `dataset/` and are ignored by Git. Use only with informed consent and document retention/deletion procedures for real deployments.

## Tests

```powershell
pytest -q
```

See `docs/TEST_CASES.md` for the testing checklist and `docs/ARCHITECTURE.md` for design decisions.
