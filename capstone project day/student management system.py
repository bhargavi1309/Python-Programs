class Student:

    def __init__(self,name,cgpa):

        self.name = name
        self.cgpa = cgpa
def display(student):

    print(student.name)

    print(student.cgpa)
student1 = Student(
    "Bhargavi",
    9.07
)
with open(
    "students.txt",
    "a"
) as file:

    file.write(
        f"{student1.name},{student1.cgpa}\n"
    )
#output: Bhargavi,9.07 in students.txt