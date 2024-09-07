               # 28-08-24
from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        seen = set()
        
        for num in arr:
            if (num + x) in seen or (num - x) in seen:
                return 1
            seen.add(num)
        
        return -1
obj=Solution()
n = 6
x = 78
arr = [5, 20, 3, 2, 5, 80]
print(obj.findPair(n,x,arr))