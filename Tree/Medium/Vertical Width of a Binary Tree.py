                    # 25-08-24
def verticalWidth(root):
    # code here
    if not root:
        return 0
    hd_set=set()
    q=[(root,0)]
    
    while q:
        node,hd=q.pop(0)
        hd_set.add(hd)
        if node.left:
            q.append((node.left,hd-1))
        if node.right:
            q.append((node.right,hd+1))
    return len(hd_set)
        
    
    '''
              # WRONG  -- not read the question properly
    def height(root):
        if root is None:
            return 0
        lh=height(root.left)
        rh=height(root.right)
        return max(lh,rh) + 1
    if root is None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return lh + rh + 1
    '''


    