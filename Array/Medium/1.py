                       # 28-08-24
                       #Sorting Elements of an Array by Frequency

class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code here
        d=dict()
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        print(d)
        return sorted(d)


arr= [5, 5, 4, 6, 4]
obj=Solution()
print(obj.sortByFreq(arr))