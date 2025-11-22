"""
Name: Nikhil Bhiduri
Roll no: 2501010128
Date: 22/11/2025
"""

import csv

# Analyse Funcs
def calc_avg(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calc_median(marks_dict):
    values = sorted(marks_dict.values())
    n = len(values)
    mid = n // 2
    return values[mid] if n%2 != 0 else (values[mid - 1] + values[mid]) / 2

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

# Grade Assignment

def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

def grade_distribution(grades):
    distri = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades.values():
        distri[g] += 1
    return distri

# Input Method

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student's name: ")
        try:
            score = int(input("Enter marks: "))
        except ValueError:
            print("Invalid Entry! skipping this student")
            continue
        
        marks[name] = score
    return marks

def load_csv():
    filename = input("Enter CSV filename (with .csv): ")
    marks = {}
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                marks[row[0]] = int(row[1])
    except FileNotFoundError:
        print("File not found! Try again.")
    return marks

# Pass/Fail Filter

def pass_fail_lists(marks_dict):
    passed = [name for name, mark in marks_dict.items() if mark >= 40]
    failed = [name for name, mark in marks_dict.items() if mark < 40]
    return passed, failed

# CSV Export

def export_results_to_csv(marks_dict, grades):
    filename = input("Enter filename to export (e.g., results.csv): ")
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Marks", "Grade"])  # header

            for name in marks_dict:
                writer.writerow([name, marks_dict[name], grades[name]])

        print(f"Results exported successfully to {filename}")

    except Exception as e:
        print("Error exporting CSV:", e)

# Display Table

def display_table(marks_dict, grades):
    print("\nName\tMarks\tGrade")
    print("-"*50)
    for name in marks_dict:
        print(f"{name}\t{marks_dict[name]}\t{grades[name]}")

# Main CLI

def main():
    print("="*50)
    print("      Welcome to GradeBook Analyzer")
    print("="*50)
    print("\n")

    while True:
        print("\nChoose Input Method:")
        print("1. Manual Entry")
        print("2. Load from CSV")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            marks = manual_input()

        elif choice == "2":
            marks = load_csv()

        elif choice == "3":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
            continue

        if not marks:
            print("No data loaded. Try again!")
            continue

        # Compute statistics
        avg = calc_avg(marks)
        med = calc_median(marks)
        maximum = find_max_score(marks)
        minimum = find_min_score(marks)

        print("\n----- Statistical Summary -----")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {med}")
        print(f"Highest Score: {maximum}")
        print(f"Lowest Score: {minimum}")

        # Grades
        grades = assign_grades(marks)
        dist = grade_distribution(grades)

        print("\n----- Grade Distribution -----")
        for grade, count in dist.items():
            print(f"{grade}: {count}")

        # Pass / Fail
        passed, failed = pass_fail_lists(marks)
        print("\n----- Pass / Fail Summary -----")
        print(f"Passed Students ({len(passed)}): {passed}")
        print(f"Failed Students ({len(failed)}): {failed}")

        # Table
        print("\n----- Results Table -----")
        display_table(marks, grades)

        # Export result

        export_choice = input("\nDo you want to export the final table to a CSV file? (y/n): ")
        if export_choice.lower() == "y":
            export_results_to_csv(marks, grades) 

        # Continue?
        again = input("\nDo you want to analyze again? (y/n): ")
        if again.lower() != "y":
            print("Goodbye! Thank you")
            break




if __name__ == "__main__":
    main()
