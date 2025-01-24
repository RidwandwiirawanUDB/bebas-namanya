from university import University

class Course:
    def __init__(self, course_name, course_code, department):
        self.course_name = course_name
        self.course_code = course_code
        self.department = department
        self.students = []  # List of students enrolled in the course.

    def __str__(self):
        return f"{self.course_name} ({self.course_code}), Department: {self.department}"

    @classmethod
    def create_course(cls):
        name = input("Enter course name: ")
        code = input("Enter course code: ")
        department_name = input("Enter department name: ")
        department = next((d for d in University.departments if d.name == department_name), None)
        if department:
            University.courses.append(cls(name, code, department))
            print("Course added successfully!\n")
        else:
            print("Department not found.\n")

    @classmethod
    def assign_student(cls):
        course_code = input("Enter course code: ")
        student_id = input("Enter student ID: ")

        course = next((c for c in University.courses if c.course_code == course_code), None)
        student = next((s for s in University.students if s.student_id == student_id), None)

        if course and student:
            if student not in course.students:
                course.students.append(student)
                print(f"Student {student.name} has been added to {course.course_name}.\n")
            else:
                print(f"Student {student.name} is already enrolled in {course.course_name}.\n")
        else:
            print("Course or Student not found.\n")

    @classmethod
    def assign_schedule(cls):
        course_code = input("Enter course code: ")
        professor_id = input("Enter professor ID: ")
        building_name = input("Enter building name: ")
        room_number = input("Enter room number: ")
        time = input("Enter schedule time (e.g., Tue 12:00-14:00): ")

        course = next((c for c in University.courses if c.course_code == course_code), None)
        professor = next((p for p in University.professors if p.professor_id == professor_id), None)
        building = next((b for b in University.buildings if b.name == building_name), None)
        room = next((r for r in building.rooms if r.room_number == room_number), None) if building else None

        if course and professor and room:
            if not course.students:
                print(f"No students are assigned to the course {course.course_name}. Schedule not created.")
                return

            schedule = {
                "course": course,
                "professor": professor,
                "room": room,
                "time": time,
                "students": course.students  # Include enrolled students in the schedule.
            }
            University.schedules.append(schedule)
            print(f"Schedule for {course.course_name} added successfully!\n")
        else:
            print("Invalid course, professor, building, or room.\n")
