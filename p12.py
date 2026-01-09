# Program to swap two number without using third variable.
a = int(input("Enter first number : ")) 
b = int(input("Enter Second number :"))
print("Before Swapping \n a=" + str(a) + "\t b=" +str(b))
a = a+b
b = a-b
a = a-b
print("After Swapping \n a=" + str(a) + "\t b=" +str(b))