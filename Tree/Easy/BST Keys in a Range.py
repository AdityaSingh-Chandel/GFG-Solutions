                        # 23-08-24
class Solution:
    def printNearNodes(self, root, low, high):
        #code here.
        def inOrder(root):
            if root is None:
                return []
            return inOrder(root.left)+[root.data]+inOrder(root.right)
        arr=inOrder(root)
        
        i=0
        while arr[i]<low and i<len(arr)-1:
            i+=1
        if i>=len(arr)-1:
            return []
        j=len(arr)-1       # IMPORTANT
        while arr[j]>high:
            j-=1
        
        return arr[i:j+1]