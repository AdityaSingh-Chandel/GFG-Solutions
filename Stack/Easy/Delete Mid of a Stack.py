                    # 07-09-24
class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        s2=[]
        for i in range(sizeOfStack//2):
            s2.append(s.pop())
        s.pop()
        while s2:
            s.append(s2.pop())
        return s