                    # 25-08-24
class Solution:
    
    def diameter(self, root):
        res = [-float('inf')]
        
        def dia(root):
            if root is None:
                return 0
            
            lh = dia(root.left)          # lh ==> lh
            rh = dia(root.right)        # rh ==> rh
            
            res[0] = max(res[0], 1 + lh + rh)
            
            return 1 + max(lh, rh)
        
        dia(root)
        return res[0]      # 'res' is storing the max width(diameter)