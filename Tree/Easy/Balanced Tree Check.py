                            # 23-08-24
class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self,root):
        #add code here
        def height(root):
            if root is None:
                return 0
            
            lh=height(root.left)
            if lh==-1:
                return -1
            print("root",root.data)
            print("lh:",lh)
        
            rh=height(root.right)
            if rh==-1:
                return -1
            print("rh:",rh,"  lh:",lh)
            
            if abs(lh-rh)>1:
                return -1
            return max(rh,lh) + 1
        
        return height(root)!=-1 or height(root)==0

# Driver Code

# Creating a sample binary tree:
#         1
#       /   \
#      2     3
#     / \   /
#    4   5 6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

root.left.left.left = Node(7)
root.left.left.left.left = Node(9)

obj=Solution()
print(obj.isBalanced(root))
