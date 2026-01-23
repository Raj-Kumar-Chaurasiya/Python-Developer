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

# insert any place

newNode = Node(99)
k=2
curr = head
for i in range(k-2):
    curr = curr.next
newNode.next= curr.next
curr.next=newNode


# remove any place

k=2
curr = head
for i in range(k-2):
    curr = curr.next.next
curr.next= curr.next.next

link(head)