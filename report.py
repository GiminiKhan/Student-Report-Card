class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        percent = self.percentage()
        if percent >= 80:
            return 'A+'
        elif percent >= 70:
            return 'A'
        elif percent >= 60:
            return 'B'
        elif percent >= 50:
            return 'C'
        elif percent >= 40:
            return 'F'
        else:
            return 'Fail'

    def display_report_card(self):
        print(f"\nReport Card for {self.name} (Roll Number: {self.roll_number})")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Total Marks: {self.total_marks()}")
        print(f"Percentage: {self.percentage():.2f}%")
        print(f"Grade: {self.grade()}")


def main():
    students = []

    while True:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = {
            'Math': int(input("Enter marks for Math: ")),
            'Physics': int(input("Enter marks for Physics: ")),
            'Urdu': int(input("Enter marks for Urdu: ")),
            'English': int(input("Enter marks for English: ")),
            'Computer': int(input("Enter marks for Computer: "))
        }

        student = Student(name, roll_number, marks)
        students.append(student)

        print(f"Record of {name} inserted successfully.")
        more = input("Do you want to insert more? Press 'Y' for Yes or 'N' for No: ").strip().upper()
        if more != 'Y':
            break

    print("\nAll Students Report Cards:")
    for student in students:
        student.display_report_card()


if __name__ == "__main__":
    main()
