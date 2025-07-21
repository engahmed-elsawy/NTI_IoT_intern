def student_grade_manager():
    # Ask the user how many students
    num_students = int(input("How many students? "))
    
    # For each student, input their name and grade
    student_grades = {}
    for _ in range(num_students):
        name = input("Enter student name: ")
        grade = float(input(f"Enter grade for {name}: "))
        student_grades[name] = grade

    print("\n--- Results ---")

    # Print all students with their grades
    print("\nAll students and their grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

    # Highest grade and student name
    highest_student = max(student_grades, key=student_grades.get)
    print(f"\nHighest grade: {student_grades[highest_student]} (Student: {highest_student})")

    # Average grade
    average = sum(student_grades.values()) / len(student_grades)
    print(f"\nAverage grade: {average:.2f}")

    # Students who failed (grade < 50)
    print("\nStudents who failed (grade < 50):")
    failed_students = [name for name, grade in student_grades.items() if grade < 50]
    if failed_students:
        for name in failed_students:
            print(f"{name}: {student_grades[name]}")
    else:
        print("No students failed.") 

# Run the program
student_grade_manager()

