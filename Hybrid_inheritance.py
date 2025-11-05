class A:
    def display(self):
        print("In Class A")

class B(A):
    def display1(self):
        print("In Class B")

class C(A):
    def display2(self):
        print("In Class C")

class D(B,C):
    def display3(self):
        print("In Class D")

x = D()
x.display()
x.display1()
x.display2()
