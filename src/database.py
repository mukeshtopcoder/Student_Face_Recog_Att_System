import os
from contextlib import contextmanager
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()


DB_CONFIG = {
    "host": os.getenv("DB_HOST","localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user":os.getenv("DB_USER", 'root'),
    "password": os.getenv("DB_PASSWORD", ""),
    'database': os.getenv("DBNAME","cv_attendance"),
}

class DatabaseError(Exception):
    pass

@contextmanager
def get_connection():
    """" Context manager that yields a MYSQL connection and always closes it, even if an exception occurs."""
    conn = None
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("Connected")
        yield conn
    except Error as e:
        raise DatabaseError(f"Could not Connect to the database: {e}")
    finally:
        if conn is not None and conn.is_connected():
            conn.close()


def test_connection()-> bool:
    """Used by the dashboard/admin page to show db health"""
    print("Testing database connection...")
    try:
        with get_connection():
            return True
    except DatabaseError:
        return False
print("database Connected.")

###
test_connection()


## STUDENT CRUD

def add_student(student_id, name, email, phone, course):
    query = """
    INSERT INTO students (student_id, name, email, phone, course)
    VALUES(%s, %s, %s, %s, %s)
"""

    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query, (student_id, name, email, phone, course))
            conn.commit()
        except Error as e:
            conn.rollback()
            if e.errno == 1062:   # duplicate primary key
                raise DatabaseError(f"Student ID '{student_id}' already exists.")
            raise DatabaseError(f"Failed to add student:{e}")
        finally:
            cursor.close()


add_student(
    "101",
    "Akash",
    "akash@gmail.com",
    "9876543210",
    "B.Tech CSE"
)