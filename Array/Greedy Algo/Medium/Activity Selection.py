                             # 26-08-24
class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        arr=[]
        for i in range(n):
            arr.append((start[i],end[i]))
        arr.sort(key=lambda x : x[1])
        res=1
        prev=0
        for i in range(1,n):
            if arr[i][0]>arr[prev][1]:
                res+=1
                prev=i
        return res