from datetime import date, datetime
from .database import execute

def mark_attendance(student_id: str):
    today = date.today()
    existing = execute("SELECT id FROM attendance WHERE student_id=%s AND attendance_date=%s", (student_id, today), True)
    if existing:
        return False, "Attendance already recorded for today."
    execute("INSERT INTO attendance (student_id, attendance_date, attendance_time) VALUES (%s,%s,%s)",
            (student_id, today, datetime.now().time()))
    return True, "Attendance marked successfully."

def fetch_attendance(student_id=None, start_date=None, end_date=None):
    query = "SELECT a.student_id, s.name, s.course, a.attendance_date, a.attendance_time, a.status FROM attendance a JOIN students s ON s.student_id=a.student_id WHERE 1=1"
    params = []
    if student_id:
        query += " AND a.student_id=%s"; params.append(student_id)
    if start_date:
        query += " AND a.attendance_date >= %s"; params.append(start_date)
    if end_date:
        query += " AND a.attendance_date <= %s"; params.append(end_date)
    return execute(query + " ORDER BY a.attendance_date DESC, a.attendance_time DESC", params, True)
