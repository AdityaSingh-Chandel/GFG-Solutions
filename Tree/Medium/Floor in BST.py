              #end July'24
def floor(root, x):
    # Initialize result as None
    res = -1
    
    # Traverse the tree
    while root is not None:
        if root.data == x:
            return root.data
        if root.data > x:
            root = root.left
        else:
            res = root.data
            root = root.right
    return res