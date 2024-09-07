                            #23-08-24
'''
  # APPROACH:-
  Inorder of BST---> Sorted 
  reverse inorder-- i.e.--> right->root->left
'''  
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        #your code here
        def revIn(root):
            if root is None:
                return []
            return revIn(root.right) +[root.data] +revIn(root.left)
        arr=revIn(root)
        return arr[k-1]

# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
obj=Solution()
print(obj.InOrder(root))  
    
