import pdfplumber
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = r"C:\Users\Mukesh\Desktop\Computer_Vision_Attendance_System_Student_Project_Guide.pdf"
with pdfplumber.open(path) as pdf:
    for index, page in enumerate(pdf.pages, 1):
        print(f"=== PAGE {index} ===")
        print(page.extract_text() or "")
