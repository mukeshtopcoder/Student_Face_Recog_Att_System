# Architecture

`app.py` handles login and navigation. Streamlit pages are thin UI layers. Business rules live in `src/`, with separate services for database access, authentication, students, attendance, and computer vision.

Face embeddings are saved as NumPy files and referenced in MySQL. Attendance uses a pre-insert duplicate check plus a MySQL unique constraint on `(student_id, attendance_date)`. Unknown faces and frames containing zero or multiple faces are rejected.
