# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursive(node: TreeNode, range: tuple) -> bool:
            if not node:
                return True

            if node.val < range[0] or node.val > range[1]:
                return False

            return revursive(node.left, (range[0], node.val - 1)) and recursive(node.right, (node.val + 1, range[1]))

        return recursive(root, (-2**31, (2**31) - 1))
