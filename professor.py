from person import Person
from university import University

class Professor(Person):
    def __init__(self, name, age, email, professor_id):
        super().__init__(name, age, email)
        self.professor_id = professor_id
        self.schedule = []

    def __str__(self):
        return f"{super().__str__()}, ID: {self.professor_id}"

    @classmethod
    def register(cls):
        name = input("Enter professor's name: ")
        age = int(input("Enter professor's age: "))
        email = input("Enter professor's email: ")
        professor_id = input("Enter professor ID: ")
        University.professors.append(cls(name, age, email, professor_id))
        print("Professor registered successfully!\n")
