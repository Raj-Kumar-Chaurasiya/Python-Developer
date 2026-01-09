class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def search(root,key):
    if root is None or root.key == key:
        return root
    if root.key<key:
        return search(root.right,key)
    return search(root.left,key)



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
print("Found" if search(root, 19) else "Not Found")
print("Found" if search(root, 1) else "Not Found")
    