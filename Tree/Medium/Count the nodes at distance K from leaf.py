                  # 25-08-24
'''
@input - 
node - root node of given tree
k = distance of nodes required 
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
class Solution:
    def printKDistantfromLeaf(self, root, k):
        # To keep track of special nodes
        self.special_nodes = set()
        
        # Start DFS traversal
        self.find_special_nodes(root, k, [], 0)
        
        # Return the count of special nodes
        return len(self.special_nodes)
    
    def find_special_nodes(self, node, k, path, path_len):
        # Base case
        if node is None:
            return
        
        # If we need to expand the path array (first time visiting this node)
        if len(path) > path_len:
            path[path_len] = node
        else:
            path.append(node)
        
        path_len += 1
        
        # If this is a leaf node, check the path for nodes at distance k
        if node.left is None and node.right is None:
            # Check if the node at path_len - k - 1 exists and is valid
            if path_len - k - 1 >= 0:
                print("path:",path_len)
                self.special_nodes.add(path[path_len - k - 1])
            return
        
        # Recur for left and right children
        self.find_special_nodes(node.left, k, path, path_len)
        self.find_special_nodes(node.right, k, path, path_len)

'''
class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        #code here
        if root is None:
            return -1
        ans=0
        if k==0:
            if self.kdist(root,k):
                ans+=1
        else:
            self.printKDistantfromLeaf(root.left, k-1)
            self.printKDistantfromLeaf(root.right, k-1)
    def kdist(self,root,k):
        if root is None:
            return 
        if k==0 and root.left==None and root.right==None:
            return True
        else:
            self.kdist(root.left,k-1)
            self.kdist(root.right,k-1)
'''        
# Driver Code

# Manually constructing the tree based on the given structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.right.left.right = Node(8)

# Function to print level-order traversal of the tree
from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(str(node.data))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(" ".join(result))

# Performing level-order traversal to check the tree structure
level_order_traversal(root)  # Expected Output: 1 2 3 4 5 6 7 8

# call
k = 2
obj=Solution()
print(obj.printKDistantfromLeaf(root, k))
