from university import University

class Department:
    def __init__(self, name, head):
        self.name = name
        self.head = head

    def __str__(self):
        return f"Department: {self.name}, Head: {self.head}"

    @classmethod
    def add_department(cls):
        name = input("Enter department name: ")
        head = input("Enter department head's name: ")
        University.departments.append(cls(name, head))
        print("Department added successfully!\n")

    @classmethod
    def view_departments(cls):
        for department in University.departments:
            print(department)
