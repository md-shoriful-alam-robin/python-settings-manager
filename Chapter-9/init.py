


class Student:
    schoolName = "ABC School"

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Course: {self.course}, School: {self.schoolName}"

student1 = Student("Khushi", "Btech")
print(student1)

student2 = Student("Ankit", "Bsc")
print(student2)

