                      # 25-08-24
'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

#Function to return a tree created from postorder and inoreder traversals.
class Solution:
    pos_idx=0
    def buildTree(self,n , In, post):
        # your code here
        Solution.pos_idx=n-1
        
        mp={}
        for i in range(n):
            mp[In[i]]=i
        
        return self.bTree(n,In,post,0,n-1,mp)
    
    def bTree(self,n,In,post,isi,iei,mp):
        if isi>iei:
            return 
        root=Node(post[Solution.pos_idx])
        Solution.pos_idx-=1
        
        if isi==iei:
            return root
        
        i=mp[root.data]
        
        #root.left=self.bTree(n,In,post,isi,i-1,mp)
        root.right=self.bTree(n,In,post,i+1,iei,mp)
        #-----    # LEFT below RIGHT    ----
        root.left=self.bTree(n,In,post,isi,i-1,mp)
        
        return root