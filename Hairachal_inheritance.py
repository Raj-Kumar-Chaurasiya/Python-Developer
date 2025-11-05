class A:
    def display(self):
        print("In Class A")

class B(A):
    def display(self):
        A.display(self)
        print("In Class B")

class C(A):
    def display(self):
        A.display(self)
        print("In Class C")

class D(A):
    def display(self):
        A.display(self)
        print("In Class D")

x = B()
y = C()
z = D()
x.display()
y.display()
z.display()