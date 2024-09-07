                  # 18-08-24

class Solution:
    def canSplit(self, arr):
        #code here
        Asum=sum(arr)
        lSum=0
        
        for i in range(len(arr)-1):
            lSum+=arr[i]
            Rsum=Asum-lSum
            
            if Rsum==lSum:
                return True
        return False