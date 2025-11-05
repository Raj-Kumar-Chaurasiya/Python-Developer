class GrandFather:
    def name(self):
        print(" the name is Dasharath")

class Parent(GrandFather):
    def age(self):
        print("The Age is :23")

class Child(Parent):
    def course(self):
        print(" the course")
    

c=Child()
c.name()
c.age()
c.course()
