            # Max Sum with No Consecutives
                  # 18-08-24

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        prev_prev=a[0]
        prev=max(a[0],a[1])
        res=prev
        
        for i in range(3,n+1):
            res=max(prev,prev_prev+a[i-1])
            prev_prev=prev
            prev=res
        return res
    
