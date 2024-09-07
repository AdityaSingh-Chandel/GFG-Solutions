                                 # 26-08-24
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        # code here
        arr.sort(key=lambda x : x.value/x.weight, reverse =True)
        ans=0.0
        for x in arr:
            if w>=x.weight:
                w-=x.weight
                ans+=x.value
            else:
                ans+=x.value * w / x.weight
                break
        return ans