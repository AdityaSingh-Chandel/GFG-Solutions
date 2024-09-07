                        # 23-08-24
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        if root.left is None:
            return self.minDepth(root.right) + 1
        
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
