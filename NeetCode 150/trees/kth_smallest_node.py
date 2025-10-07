# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.counter = 0

        def inorder(node: TreeNode):
            if node is None:
                self.counter += 1
                return None

            l = inorder(node.left)
            if l is not None:
                return l

            if self.counter == k:
                return node.val

            r = inorder(node.right)
            if r is not None:
                return r

        return inorder(root)
