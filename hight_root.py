class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def height(root):
    if root is None:
        return -1


    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight,rheight)+1

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

    root.right.left.left.left=Node(12)

    print(height(root))