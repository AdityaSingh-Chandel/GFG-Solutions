                     # 25-08-24
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
from collections import deque
#Function to make binary tree from linked list.
def convert(head):
  
    # code here
    if not head:
        return 
    root=Tree(head.data)
    curr=head.next
    q=deque([root])
    while curr:
        parent=q.popleft()
        
        lc=Tree(curr.data)
        parent.left=lc
        q.append(lc)
        
        if curr.next!=None:
            curr=curr.next
        else:
            break
        
        rc=Tree(curr.data)
        parent.right=rc
        q.append(rc)
        
        curr=curr.next
    
    return root

# Driver Code
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

print(convert(head))