        # RECURSIVE
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        # code here
        n=len(wt)
        def knap(W,wt,val,n):
            if W==0 or n==0:
                return 0
            if wt[n-1]>W:
                return knap(W,wt,val,n-1)
            else:
                return max(val[n-1]+knap(W-wt[n-1],wt,val,n-1) , knap(W,wt,val,n-1))
        return knap(W,wt,val,n)
        