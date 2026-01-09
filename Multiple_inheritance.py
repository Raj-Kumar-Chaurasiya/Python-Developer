# Multiple Inheritance Example

class Person:
    def __init__(self,name):
        self.name=name
    
class Course:
    def __init__(self,course):
        self.course=course

class StudentCourse(Person,Course):
    def __init__(self, name, course):
        Person.__init__(self, name)
        Course.__init__(self,course)

    def enroll(self):
        print(f"{self.name} has enrolled in {self.course}")

s=StudentCourse("Ram", " Python ")
s.enroll()