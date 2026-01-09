class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def find_p(root,target,parent):
    if root is None:
        return -1
    
    if root.data ==target:
        return parent
    
    left=find_p(root.left,target,root.data)

    if left !=-1:
        return left
    return find_p(root.right,target,root.data)

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
    root.right.left.right=Node(11)

    target=7

    parent= find_p(root,target, -1)

    print(parent)

    