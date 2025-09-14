# write a program to change the value in tuple.

x = ("ram","sita")
y = list(x)
y[1]="mohan"
x = tuple(y)
print(x)