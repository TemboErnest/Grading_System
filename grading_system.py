# grading_system.py
# ICT111 - Principles of Programming (Python & Git)
# Lab: Student Grading System
# Console application that records student marks, assigns grades
# and produces a class summary.

students = []  # list of dictionaries, one dictionary per student

while True:
    # ---------- MENU ----------
    print("\n===== STUDENT GRADING SYSTEM =====")
    print("1. Add student")
    print("2. Display all")
    print("3. Class summary")
    print("4. Exit")
    option = input("Choose 1-4: ").strip()

    # ---------- OPTION 1: Aent ---")

        # Validate student number (must not be blank)
        student_number = input("Enter student number: ").strip()
        while student_number == "":
            print("Error: student number cannot be blank.")
            student_number = input("Enter student number: ").strip()

        # Validate name (muDD STUDENT ----------
    if option == "1":
        print("\n--- Add Studst not be blank)
        name = input("Enter student name: ").strip()
        while name == "":
            print("Error: name cannot be blank.")
            name = input("Enter student name: ").strip()

        # Validate mark (numeric and between 0 and 100) - re-prompt until valid
        mark = None
        while mark is None:
            mark_text = input("Enter mark (0-100): ").strip()
            try:
                value = float(mark_text)
            except ValueError:
                print("Error: mark must be a number. Please try again.")
                continue

            if value < 0 or value > 100:
                print("Error: mark must be between 0 and 100. Please try again.")
            else:
                mark = value

        # Work out grade and decision using if/elif/else
        if mark >= 80:
            grade = "A"
            decision = "Excellent"
        elif mark >= 70:
            grade = "B"
            decision = "Very good"
        elif mark >= 60:
            grade = "C"
            decision = "Good"
        elif mark >= 50:
            grade = "D"
            decision = "Pass"
        else:
            grade = "F"
            decision = "Fail"

        # Store the record as a dictionary inside the students list
        record = {
            "student_number": student_number,
            "name": name,
            "mark": mark,
            "grade": grade,
            "decision": decision,
        }
        students.append(record)

        # Clear feedback
        print("\nRecord added successfully!")
        print(f"{name} ({student_number}) scored {mark:.1f} -> Grade {grade} ({decision})")

    # ---------- OPTION 2: DISPLAY ALL ----------
    elif option == "2":
        print("\n--- Student Report ---")
        if len(students) == 0:
            print("No student records found. Please add a student first (option 1).")
        else:
            print(f"{'No.':<5}{'Student No.':<15}{'Name':<25}{'Mark':<8}{'Grade':<7}{'Decision'}")
            print("-" * 72)
            count = 1
            for s in students:
                print(f"{count:<5}{s['student_number']:<15}{s['name']:<25}"
                      f"{s['mark']:<8.1f}{s['grade']:<7}{s['decision']}")
                count += 1

    # ---------- OPTION 3: CLASS SUMMARY ----------
    elif option == "3":
        print("\n--- Class Summary ---")
        if len(students) == 0:
            print("No students have been added yet, so there is no summary to show.")
        else:
            total = 0
            total_marks = 0
            highest = students[0]["mark"]
            lowest = students[0]["mark"]
            passes = 0
            fails = 0

            for s in students:
                total += 1
                total_marks += s["mark"]
                if s["mark"] > highest:
                    highest = s["mark"]
                if s["mark"] < lowest:
                    lowest = s["mark"]
                if s["mark"] >= 50:
                    passes += 1
                else:
                    fails += 1

            average = total_marks / total  # safe: total is at least 1 here

            print(f"Total students : {total}")
            print(f"Class average  : {average:.2f}")
            print(f"Highest mark   : {highest:.1f}")
            print(f"Lowest mark    : {lowest:.1f}")
            print(f"Passes (>= 50) : {passes}")
            print(f"Fails  (< 50)  : {fails}")

    # ---------- OPTION 4: EXIT ----------
    elif option == "4":
        print("\nThank you for using the Student Grading System. Goodbye!")
        break

    # ---------- INVALID OPTION ----------
    else:
        print("Invalid option! Please enter 1, 2, 3 or 4.")
