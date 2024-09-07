                    # 23-08-24
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return list containing elements of right view of binary tree.
    from collections import deque
    def rightView(self,root):
        
        # code here
        if root is None:
            return []
        q=deque([(root,0)])
        r_view=[]
        mx_lev=-1
        
        while q:
            node,lev=q.popleft()
            if lev>mx_lev:
                r_view.append(node.data)
                mx_lev=lev
            if node.right:
                q.append((node.right,lev+1))
            if node.left:
                q.append((node.left,lev+1))
        return r_view