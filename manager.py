import json
import os
from student import Student

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.students = [Student(s["id"], s["name"], s["grade"]) for s in data]

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=2)

    def id_exists(self, student_id):
        return any(s.student_id == student_id for s in self.students)

    def add(self, student_id, name, grade):
        if self.id_exists(student_id):
            print("Error: ID already exists!")
            return
        self.students.append(Student(student_id, name, grade))
        self.save()
        print("Student added successfully.")

    def update(self, student_id, name, grade):
        for s in self.students:
            if s.student_id == student_id:
                s.name = name
                s.grade = grade
                self.save()
                print("Student updated.")
                return
        print("Student not found.")

    def delete(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
        self.save()
        print("Student deleted.")

    def list_all(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            s.display()
