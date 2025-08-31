# Program to display and sort list elements.
list = []
n = int(input("Enter range: "))
for i in range(0,n):
    el = int(input())
    list.append(el)
list.sort()
print("Sorted Element in ascending order ")
print(list)
list.reverse()
print("Sorted Element in descending order")
print(list)