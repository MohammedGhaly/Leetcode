class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        hm = {None: None}
        h = head
        while h is not None:
            hm[h] = Node(h.val)
            h = h.next

        h = head
        while h is not None:
            hm[h].next = hm[h.next]
            hm[h].random = hm[h.random]
            h = h.next

        return hm[head]
