# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        p1 = list1
        p2 = list2
        temp = None
        r = None

        if p1.val < p2.val:
            r = p1
            p1 = p1.next
        else:
            r = p2
            p2 = p2.next

        result = r

        while not (p1 == None or p2 == None):
            if (p1.val < p2.val):
                r.next = p1
                p1 = p1.next
            else:
                r.next = p2
                p2 = p2.next
            r = r.next

        if p1 == None:
            r.next = p2

        if p2 == None:
            r.next = p1

        return result
