class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:

    def hasCycle(self, head: ListNode) -> bool:
        pos = -1
        if head is None:
            return False
        hash_set = set()
        hash_set.add(head)
        while True:
            if head.next is None:
                return False
            if head.next not in hash_set:
                hash_set.add(head.next)
                head = head.next
                pos += 1
            else:
                return True

        return False


class Solution2:
    # better memory O(1)
    def hasCycle(self, head: ListNode) -> bool:
        pos = -1
        while head is not None:
            if head.val > 100_000:
                return True
            else:
                head.val = 200_000

            head = head.next
            pos += 1

        return False
