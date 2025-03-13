import streamlit as st

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
        st.write(f"\n**Report Card for {self.name} (Roll Number: {self.roll_number})**")
        for subject, mark in self.marks.items():
            st.write(f"{subject}: {mark}")
        st.write(f"**Total Marks:** {self.total_marks()}")
        st.write(f"**Percentage:** {self.percentage():.2f}%")
        st.write(f"**Grade:** {self.grade()}")

st.title("Student Report Card Generator")

students = []

name = st.text_input("Enter student name")
roll_number = st.text_input("Enter roll number")
marks = {
    'Math': st.number_input("Enter marks for Math", min_value=0, max_value=100, step=1),
    'Physics': st.number_input("Enter marks for Physics", min_value=0, max_value=100, step=1),
    'Urdu': st.number_input("Enter marks for Urdu", min_value=0, max_value=100, step=1),
    'English': st.number_input("Enter marks for English", min_value=0, max_value=100, step=1),
    'Computer': st.number_input("Enter marks for Computer", min_value=0, max_value=100, step=1)
}

if st.button("Insert Record"):
    student = Student(name, roll_number, marks)
    students.append(student)
    st.success(f"Record of {name} inserted successfully.")

if st.button("Show All Report Cards"):
    if students:
        for student in students:
            student.display_report_card()
    else:
        st.warning("No student records available.")
