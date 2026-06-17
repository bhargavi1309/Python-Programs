class Student:

    def __init__(self, name, branch, cgpa):

        self.name = name
        self.branch = branch
        self.cgpa = cgpa

    def display(self):

        print("Name:", self.name)
        print("Branch:", self.branch)
        print("CGPA:", self.cgpa)
student1 = Student(
    "Bhargavi",
    "CSE(AI)",
    9.07
)

student1.display()
