# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapPairs(self, head: ListNode):
        if head is None or head.next is None :
            return head
        
        head_after_swap = head.next
        
        def dfs(h:ListNode, i:int):
            if h.next is None:
                return [h] if (i%2 == 0) else [h, None]
            res = dfs(h.next, i+1)
            
            if len(res)==2:
                res[0].next = h
                h.next = res[1]
                return [res[0]]
                
            elif len(res)==1:
                return [h, res[0]]
                
        dfs(head, 0)
        return head_after_swap


sol = Solution()
n5 = ListNode(5,None)
n4 = ListNode(4,n5)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

h = sol.swapPairs(n1)
s = h
while s :
    print(s.val) 
    s=s.next