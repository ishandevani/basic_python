# 2. Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student's grade.
# Print all student grades.
# Use a dictionary and basic operations with if / else.


# -------------- Create empty dictionary to store student grades and name.
Student_grade = {}

while True:
    print("\n---Student Grades---")
    print("1. Add a new student name and grade")
    print("2. Update an exiting student's grade")
    print("3. print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name=input("Enter student name: ")
        if name in Student_grade:
            print(f"{name} already exists. Use option 2 to update.")
        else:
            grade = input(f"Enter grade for {name}: ")
            Student_grade[name] = grade
            print(f"{name} added with grade {grade}")

    elif choice == "2":
        name=input("Enter student name to update: ")
        if name in Student_grade:
            grade = input(f"Enter new grade for {name}: ")
            Student_grade[name] = grade
            print(f"{name} grade update to {grade}")
        else:
            print(f"{name} not found.")

    elif choice=="3":
        if Student_grade:
            print("\n--- All Student Grades ---")
            for name,  grade in Student_grade.items():
                print(f"{name}: {grade}")

        else:
            print("No students data added yet.")

    elif choice == "4":
        print("Exitinf code.")
        break

    else:
        print("Invalid choice. Enter a number from 1 to 4.")