# manager.py

import json
import os
from student import Student

FILE_PATH = "students.json"

class StudentManager:
    def __init__(self):
        self.students = []
        self.load_from_file()

    def load_from_file(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(s) for s in data]

    def save_to_file(self):
        with open(FILE_PATH, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def id_exists(self, student_id: str) -> bool:
        return any(s.student_id == student_id for s in self.students)

    def add_student(self, student_id, name, grade):
        if self.id_exists(student_id):
            print(f"\n❌ Error: Student ID '{student_id}' already exists!")
            return
        self.students.append(Student(student_id, name, grade))
        self.save_to_file()
        print(f"\n✅ Student '{name}' added successfully!")

    def update_student(self, student_id, name=None, grade=None):
        for s in self.students:
            if s.student_id == student_id:
                if name:  s.name = name
                if grade: s.grade = grade
                self.save_to_file()
                print(f"\n✅ Student '{student_id}' updated successfully!")
                return
        print(f"\n❌ Student ID '{student_id}' not found!")

    def delete_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                self.save_to_file()
                print(f"\n✅ Student '{student_id}' deleted!")
                return
        print(f"\n❌ Student ID '{student_id}' not found!")

    def list_students(self):
        if not self.students:
            print("\n📭 No student records found.")
            return
        print("\n" + "="*45)
        print(f"| {'ID':<10} | {'Name':<20} | {'Grade':<5} |")
        print("="*45)
        for s in self.students:
            print(s)
        print("="*45)
        print(f"  Total Students: {len(self.students)}")