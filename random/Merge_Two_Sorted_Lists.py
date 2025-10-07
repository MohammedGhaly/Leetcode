# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#########################################


class Solution(object):
    def mergeTwoLists(self, list1:ListNode, list2:ListNode) -> ListNode:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        0   2   4   6
        1   3   5   7
        """
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        p1 : ListNode = list1
        p2 : ListNode = list2
        temp : ListNode = None
        r : ListNode = None
        
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
                r = r.next
                p1 = p1.next
            else:
                r.next = p2
                r = r.next
                p2 = p2.next
                
        if p1 == None:
                r.next = p2
                 
        if p2 == None:
                r.next = p1
                
        return result
    
    
    
solution = Solution()
list1 = ListNode(0, ListNode(0, ListNode(1, ListNode(6))))
list2 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
            
result = solution.mergeTwoLists(list1, list2)

while result != None:
    print(result.val)
    result = result.next
                