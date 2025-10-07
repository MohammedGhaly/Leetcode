# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nr = TreeNode(3)
nl = TreeNode(2)
n1 = TreeNode(1, nl)
n2 = TreeNode(1, None, nl)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == q == None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


print(Solution().isSameTree(n1, n2))
