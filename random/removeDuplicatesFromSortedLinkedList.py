class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        largest = head.val
        i = head
        while i.next is not None:
            if i.next.val == largest:
                i.next = i.next.next
            else:
                largest = i.next.val
                i = i.next

        return head
