
from collections import deque
class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def InsertNode(root,data):

    if root is None:
        root=Node(data)
        return root
    
    q= deque()
    q.append(root)

    while q:
        curr = q.popleft()
        if curr.left is not None:
            q.append(curr.left)
        else:
            curr.right= Node(data)
            return root
        
        if curr.right is not None:
            q.append(curr.right)
        else:
            curr.right= Node(data)
            return root
def inorder(curr):
    if curr is None:
        return
    
    inorder(curr.left)
    print(curr.data,end=" ")
    inorder(curr.right)
    
    

if __name__=="__main__":

    root =Node(1)
    root.left=Node(2)
    root.right=Node(3)

    root.left.left=Node(4)
    root.left.right=Node(5)

    root.right.left=Node(6)
    root.right.right=Node(7)

    root.left.left.left=Node(8)
    root.left.left.right=Node(9)
    
    root.right.left.left=Node(10)
    root.right.left.right=Node(133)

    key=11
    root = InsertNode(root, key)
    

    inorder(root)

    