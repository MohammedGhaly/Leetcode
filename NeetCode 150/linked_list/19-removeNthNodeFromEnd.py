# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h = p = head
        for i in range(n):
            p = p.next

        if p is None:
            h = h.next
            return h

        while p.next is not None:
            p = p.next
            h = h.next

        h.next = h.next.next
        return head


sol = Solution()

# n2 = ListNode(2)
n1 = ListNode(1)

he = sol.removeNthFromEnd(n1, 1)
while he is not None:
    print(he.val)
    he = he.next
