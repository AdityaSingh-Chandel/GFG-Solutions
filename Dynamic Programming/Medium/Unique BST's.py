                      # 18-08-24
                      
class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,N):
        # code here
        dp=[0]*(N+1)
        dp[0]=1
        
        mod= 10**9+7
        for i in range(1,N+1):
            for j in range(i):
                dp[i]+=(dp[j]*dp[i-j-1])
                dp[i]=(dp[i] % mod)
        return dp[N]