l=[34,56,54,23,67,87]
t=67

found = False
for i in range(len(l)):
    if l[i]==t:
        print("found",i)
        found=True
        break
if not found:
    print("Not")