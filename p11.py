# Program to print the marksheet of a student.

marks = []
total = 0
for i in range(0,5):
    list =float(input())
    marks.append(list)
    total=total+marks[i]
per=(total/500)*100
print("Total Marks = "+ str(total))
print("Percentage = " + str(per))