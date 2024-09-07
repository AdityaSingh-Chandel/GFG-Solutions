                    # 27-08-24
from typing import List
class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        # code here
        flag=True
        for i in range(n-1):
            if flag:
                if arr[i]<arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=False
            else:
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                flag=True
        return arr 