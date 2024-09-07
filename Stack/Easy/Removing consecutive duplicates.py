'''You are given string str. You need to remove the consecutive duplicates from the given 
string using a Stack.

Input: 
aaaaaabaabccccccc

Output: 
ababc
'''
class Solution:
    
    #Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self,s):
        # code here
        s1=[]
        for i in s:
            s1.append(i)
        s2=[]
        for i in range(len(s1)):
            if s2 and s1[-1]==s2[-1]:
                s1.pop()
            else:
                s2.append(s1.pop())
        out=''
        for i in range(len(s2)):
            out+=str(s2.pop())
        return out