
# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    # If the tree is empty, return an empty list
    if not root:
        return []

    # Initialize a queue for level order traversal
    queue = [(root, 0)]  # (node, level)
    left_view = []
    max_level = -1  # to track the maximum level visited so far

    while queue:
        node, level = queue.pop(0)
        
        # If this is the first node of its level
        if level > max_level:
            left_view.append(node.data)
            max_level = level

        # Add the left and right children of the node to the queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return left_view



# Driver code
