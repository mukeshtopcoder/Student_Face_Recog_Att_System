from .database import execute

def create_student(data):
    execute("INSERT INTO students (student_id,name,email,phone,course) VALUES (%s,%s,%s,%s,%s)",
            (data["student_id"], data["name"], data.get("email"), data.get("phone"), data.get("course")))

def list_students(active_only=False):
    where = " WHERE is_active=TRUE" if active_only else ""
    return execute("SELECT * FROM students" + where + " ORDER BY name", fetch=True)

def set_active(student_id, active):
    execute("UPDATE students SET is_active=%s WHERE student_id=%s", (active, student_id))

def dashboard_metrics():
    students = execute("SELECT COUNT(*) AS n FROM students WHERE is_active=TRUE", fetch=True)[0]["n"]
    present = execute("SELECT COUNT(*) AS n FROM attendance WHERE attendance_date=CURDATE()", fetch=True)[0]["n"]
    recent = execute("SELECT a.student_id,s.name,a.attendance_date,a.attendance_time FROM attendance a JOIN students s ON s.student_id=a.student_id ORDER BY a.id DESC LIMIT 10", fetch=True)
    return {"students": students, "present": present, "absent": max(students-present, 0), "percentage": round(present/students*100, 1) if students else 0, "recent": recent}
