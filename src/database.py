from contextlib import contextmanager
import mysql.connector
from mysql.connector import Error
from .config import settings

@contextmanager
def connection():
    conn = mysql.connector.connect(host=settings.db_host, port=settings.db_port,
                                   user=settings.db_user, password=settings.db_password,
                                   database=settings.db_name)
    try:
        yield conn
    finally:
        if conn.is_connected():
            conn.close()

def execute(query, params=(), fetch=False, many=False):
    with connection() as conn:
        cursor = conn.cursor(dictionary=True)
        try:
            if many:
                cursor.executemany(query, params)
            else:
                cursor.execute(query, params)
            result = cursor.fetchall() if fetch else cursor.lastrowid
            conn.commit()
            return result
        except Error:
            conn.rollback()
            raise
        finally:
            cursor.close()

def health_check():
    try:
        execute("SELECT 1", fetch=True)
        return True, "Connected"
    except Exception as exc:
        return False, str(exc)
