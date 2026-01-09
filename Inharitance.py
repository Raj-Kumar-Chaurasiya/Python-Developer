class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print("My name is",{self.name})
        print("My Age is",{self.age})

class B(A):
    pass
    # def show(self):
    #     print("My name is",{self.name})
    #     print("My Age is",{self.age})

n=B("Ram",23)
n.show()