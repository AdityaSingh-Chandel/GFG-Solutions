                        # 26-08-24
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meet=[]
        for i in range(n):
            meet.append((start[i],end[i]))
        meet.sort(key=lambda x: x[1])
        res=1
        prev=0
        for i in range(1,n):
            if meet[i][0]>meet[prev][1]:
                res+=1
                prev=i
        return res