class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None

def level_order_r(root,level,res):
    if root is None:
        return
    
    if len(res) <= level:
        res.append([])

    res[level].append(root.data)

    level_order_r(root.left, level+1, res)
    level_order_r(root.right, level+1, res)

def level_order(root):
    res=[]
    level_order_r(root,0,res)
    return res

if __name__ == '__main__':
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)

    root.left.left=Node(4)
    root.left.right=Node(5)

    root.right.left=Node(6)
    root.right.right=Node(7)

    root.left.left.left=Node(8)

    root.left.right.left=Node(9)
    root.left.right.right=Node(10)

    root.left.right.left.left=Node(11)
    root.left.right.left.right=Node(23)
    res= level_order(root)

    for level in res:
        print(f'[{', '.join(map(str,level))}]', end='')
