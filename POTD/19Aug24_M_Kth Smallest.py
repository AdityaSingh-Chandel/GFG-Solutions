

class Solution:

    def kthSmallest(self, arr,k):
        ch=[None]*(max(arr)+1)
        print(ch)
        
        for i in range(len(arr)):
            ch[arr[i]]=1
        print(ch)
        j=0
        for i in range(len(ch)):
            if ch[i]==1:
                j+=1
            if j==k:
                return i
            
arr = [7, 10, 4, 3, 20, 15]
k = 3
obj=Solution()
print(obj.kthSmallest(arr,k))