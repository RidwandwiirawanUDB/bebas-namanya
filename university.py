class University:
    students = []
    professors = []
    courses = []
    departments = []
    buildings = []
    schedules = []

    @classmethod
    def menu(cls):
        print("Welcome to the Scheduling System for Students")
        print('''
            1. Add Student
            2. Add Professor
            3. Add Department
            4. Add Building
            5. Add Room to Building
            6. Add Course
            7. Assign Student to Course
            8. Assign Course to Schedule
            9. View Schedules
            10. Exit
        ''')
        while True:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                from student import Student
                Student.register()
            elif choice == 2:
                from professor import Professor
                Professor.register()
            elif choice == 3:
                from department import Department
                Department.add_department()
            elif choice == 4:
                from building import Building
                Building.add_building()
            elif choice == 5:
                from room import Room
                Room.add_room()
            elif choice == 6:
                from course import Course
                Course.create_course()
            elif choice == 7:
                from course import Course
                Course.assign_student()
            elif choice == 8:
                from course import Course
                Course.assign_schedule()
            elif choice == 9:
                cls.view_schedules()
            elif choice == 10:
                print("Exiting the system. Goodbye!\n")
                break
            else:
                print("Invalid choice. Try again.\n")


    @classmethod
    def view_schedules(cls):
        if not cls.schedules:
            print("No schedules available.")
            return

        student_id = input("Enter student ID to view schedules: ")

        # Find the student
        student = next((s for s in University.students if s.student_id == student_id), None)
        if not student:
            print("Student not found.")
            return

        # Filter schedules that include the student
        filtered_schedules = [s for s in cls.schedules if student in s['students']]

        if not filtered_schedules:
            print(f"No schedules found for student ID {student_id}.")
            return

        print(f"Schedules for {student.name} (ID: {student_id}):")
        for schedule in filtered_schedules:
            course = schedule['course']
            professor = schedule['professor']
            room = schedule['room']
            time = schedule['time']
            
            print(f"Course: {course.course_name} ({course.course_code}), "
                f"Professor: {professor.name}, "
                f"Room: {room.room_number} (Capacity: {room.capacity}), "
                f"Time: {time}")
