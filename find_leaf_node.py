class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None 

def pNodes(root: Node) ->None:

    if (not root):
        return
    
    if (not root.left and not root.right):
        print(root.data,end=" ")
        return
    
    if root.left:
        pNodes(root.left)

    if root.right:
        pNodes(root.right)
    

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


    pNodes(root)
    

    