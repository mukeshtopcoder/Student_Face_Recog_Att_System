# Intelligent Face Recognition Attendance System
## User Manual

This manual explains how to install, configure, and use the attendance application.

## 1. What the system does

The system allows an administrator to:

- Register students and capture a face image.
- Recognize a registered student using a camera image.
- Mark attendance automatically with the current date and time.
- Prevent duplicate attendance on the same day.
- View dashboard statistics.
- Search and deactivate students.
- Filter and export attendance reports.

The system requires administrator login before application pages can be used.

## 2. Requirements

Install the following before starting:

- Windows, macOS, or Linux
- Python 3.10 or newer
- MySQL Server 8 or newer
- A working webcam
- Internet access for the initial Python package installation

## 3. Installation

Open PowerShell or a terminal and move to the project folder:

```powershell
cd "C:\Users\Mukesh\Documents\Codex\2026-09-01\hi"
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project packages:

```powershell
pip install -r requirements.txt
```

If Windows blocks script activation, run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

Then activate the environment again.

## 4. Configure MySQL

1. Start MySQL Server.
2. Open MySQL Workbench or another MySQL client.
3. Open `database/database.sql`.
4. Run the complete script.

This creates the `cv_attendance` database and these tables:

- `students`
- `attendance`
- `users`
- `face_encodings`

## 5. Configure the application

Create a local environment file by copying `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the values with your MySQL settings:

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=cv_attendance
APP_SECRET_KEY=replace_with_a_random_secret
FACE_TOLERANCE=0.48
FACE_MODEL=hog
```

Never upload `.env` to GitHub. It contains private database credentials.

## 6. Create the first administrator

Generate a secure password hash. Replace `YourPassword123` with your own password:

```powershell
python -c "from src.authentication import hash_password; print(hash_password('YourPassword123'))"
```

Copy the printed hash. In MySQL Workbench, run:

```sql
USE cv_attendance;

INSERT INTO users (username, password_hash, role)
VALUES ('admin', 'PASTE_HASH_HERE', 'admin');
```

You can also create additional administrator accounts later from the Admin page.

## 7. Start the application

From the project folder, with the virtual environment active, run:

```powershell
streamlit run app.py
```

The application opens in a browser. If it does not open automatically, visit the local address shown in the terminal, usually:

```text
http://localhost:8501
```

## 8. Sign in

1. Enter the administrator username.
2. Enter the administrator password.
3. Select **Sign in**.

After signing in, the sidebar shows the available pages. Select **Sign out** when finished.

## 9. Register a student

1. Open **Student Registration**.
2. Enter a unique Student ID.
3. Enter the student’s full name.
4. Optionally enter email, phone, and course.
5. Allow browser access to the camera.
6. Position one face clearly in the camera preview.
7. Select **Capture**.
8. Select **Register student**.

Registration succeeds only when the image contains exactly one detectable face.

For best results:

- Use even lighting.
- Look directly at the camera.
- Keep the face fully visible.
- Avoid sunglasses, masks, and heavy shadows.
- Keep the camera stable.

The student record is stored in MySQL. The face representation is stored in the `encodings` folder, and its reference is recorded in MySQL.

## 10. Mark attendance

1. Open **Mark Attendance**.
2. Allow camera access if prompted.
3. Position exactly one registered student’s face in the camera preview.
4. Select **Capture**.
5. Review the recognized Student ID and face distance.
6. Select **Confirm and mark attendance**.

Possible results:

- **Attendance marked successfully**: a new record was saved.
- **Attendance already recorded for today**: the system prevented a duplicate.
- **Unknown face**: the face did not meet the recognition threshold.
- **Detect exactly one face**: no face or multiple faces were detected.

Unknown faces are never marked present.

## 11. View the dashboard

Open **Dashboard** to view:

- Number of active students
- Number present today
- Number absent today
- Attendance percentage
- Recent attendance records

The dashboard reads live data from MySQL.

## 12. Manage students

Open **Student Management** to:

1. Search by Student ID, name, or course.
2. Review the student’s active status.
3. Select **Deactivate** to prevent the student from being treated as active.
4. Select **Activate** to restore the student’s active status.

Deactivation does not delete historical attendance records.

## 13. Generate attendance reports

1. Open **Attendance Reports**.
2. Choose **All students** or a specific student.
3. Select the start date.
4. Select the end date.
5. Review the filtered records.
6. Select **Download CSV** or **Download Excel**.

The exported file contains the student ID, name, course, attendance date, attendance time, and status.

## 14. Create another administrator

1. Open **Admin**.
2. Enter a username.
3. Enter a password with at least 8 characters.
4. Select **Create admin**.

Passwords are stored as bcrypt hashes, not plain text.

## 15. Troubleshooting

### Database is offline

Check that:

- MySQL Server is running.
- The values in `.env` are correct.
- The database name is `cv_attendance`.
- The MySQL user has permission to access the database.
- Port `3306` is not blocked.

### Invalid username or password

Confirm that the user exists and is active:

```sql
USE cv_attendance;
SELECT username, role, is_active FROM users;
```

### Camera does not appear

- Allow camera permission in the browser.
- Close other applications using the webcam.
- Confirm that the webcam works in the operating system camera app.
- Restart the Streamlit application.

### Face is not detected

- Improve lighting.
- Move closer to the camera.
- Face the camera directly.
- Remove anything covering the face.
- Make sure only one face is visible.

### Known student is shown as unknown

The default tolerance is `0.48`. A lower value is stricter; a higher value is more permissive and can increase false matches. Change `FACE_TOLERANCE` in `.env` carefully and retest with real conditions.

### Registration fails for a duplicate Student ID

Student IDs must be unique. Use Student Management to review existing records before registering a new student.

### Excel export fails

Install the required Excel package again:

```powershell
pip install openpyxl
```

## 16. Data protection and privacy

Use this system only with proper authorization and informed consent. Do not use real student face data in public demos or public repositories.

- Keep `.env` private.
- Keep `dataset` and `encodings` private.
- Limit administrator access.
- Define how long face data and attendance records are retained.
- Delete face data when it is no longer needed.
- Do not publish personal information in screenshots or videos.

## 17. Stop the application

Return to the terminal running Streamlit and press:

```text
Ctrl + C
```

## 18. Run tests

After installing the requirements, run:

```powershell
pytest -q
```

The tests cover password hashing and saving/loading face encodings. Camera recognition and MySQL behavior should also be tested manually using the checklist in `docs/TEST_CASES.md`.
