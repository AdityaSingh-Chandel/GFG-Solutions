                     # 23-08-24
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
from collections import deque
def LeftView(root):
    
    # code here
    if root is None:
        return []
    q=deque([(root,0)])
    l_view=[]
    mx_lev=-1
    
    while q:
        node,lev=q.popleft()
        if lev>mx_lev:
            l_view.append(node.data)
            mx_lev=lev
        if node.left:
            q.append((node.left,lev+1))
        if node.right:
            q.append((node.right,lev+1))
    return l_view