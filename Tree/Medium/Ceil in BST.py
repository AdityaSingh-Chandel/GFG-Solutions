                  # end July 24
class Solution:
    def findCeil(self, root, inp):
        res = -1

        while root is not None:
            if root.key == inp:
                return root.key
            if root.key < inp:
                root = root.right
            else:
                res = root.key
                root = root.left
        
        return res