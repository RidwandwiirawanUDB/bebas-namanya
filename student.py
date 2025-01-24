from person import Person
from university import University

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.schedule = []

    def __str__(self):
        return f"{super().__str__()}, ID: {self.student_id}"

    @classmethod
    def register(cls):
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        email = input("Enter student's email: ")
        student_id = input("Enter student ID: ")
        University.students.append(cls(name, age, email, student_id))
        print("Student registered successfully!\n")
