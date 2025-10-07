# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        print(temp.val)
        while temp.next:
            temp = temp.next
            print(temp.val)


def create_list(l: list[int]) -> ListNode:
    head = ListNode(l[0])
    temp = head
    for i in range(1, len(l)):
        temp.next = ListNode(l[i])
        temp = temp.next
    temp.next = None
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = None

        while (l1 or l2):

            if l1 and l2:
                add = l1.val + l2.val + carry
                res = (add) % 10
                l1 = l1.next
                l2 = l2.next

            elif l1 and not l2:
                add = l1.val + carry
                res = (add) % 10
                l1 = l1.next

            elif l2 and not l1:
                add = l2.val + carry
                res = (add) % 10
                l2 = l2.next

            if not head:
                result_list = head = ListNode(res)
            else:
                head.next = ListNode(res)
                head = head.next

            carry = add // 10

        if (carry > 0):
            head.next = ListNode(carry)
        return result_list


sol = Solution()
l1 = create_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_list([9, 9, 9, 9])
sol.addTwoNumbers(l1, l2).print_list()
