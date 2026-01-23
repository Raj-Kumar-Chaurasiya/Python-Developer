class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def link(head):
    curr=head
    while curr!=None:
        print(curr.data,end="->")
        curr = curr.next
    print()

a=Node(5)
b=Node(6)
c=Node(9)

a.next=b
b.next=c
c.next=None
head=a

#insert in end
newNode = Node(88)
curr=head
while curr.next!=None:
   curr = curr.next
curr.next = newNode

#remove in end
curr=head
while curr.next.next!=None:
   curr = curr.next
curr.next = None

link(head)