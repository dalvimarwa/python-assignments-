# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"

# Main Program
marks = float(input("Enter the student's marks: "))

grade = calculate_grade(marks)

print("The student's grade is:", grade)
