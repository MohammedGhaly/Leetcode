class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return
        slow = head
        fast = head.next
        # finding the start of the flipping stack
        while True:
            if fast is None:
                break
            elif fast.next is None:
                slow = slow.next
                break
            else:
                slow = slow.next
                fast = fast.next.next

        stack = []
        flip_part = slow.next
        slow.next = None
        # storing the second part nodes in a stack
        while flip_part is not None:
            stack.append(flip_part)
            flip_part = flip_part.next

        h = head
        while h is not None and len(stack) > 0:
            h2 = h.next
            h.next = stack.pop()
            h.next.next = h2
            h = h2


# n5 = ListNode(5)
# n4 = ListNode(4)
# n3 = ListNode(3)
# n2 = ListNode(2)
# n1 = ListNode(1)
head = ListNode(0)

sol = Solution()
sol.reorderList(head)

while head is not None:
    print(head.val)
    head = head.next

# n6 = ListNode(6)
