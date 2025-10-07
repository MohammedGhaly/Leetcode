# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root: TreeNode) -> (bool, int):
            if root is None:
                return (True, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            if not isBalanced:
                return (False, max(left[1], right[1]) + 1)

            height = 1 + max(left[1], right[1])

            return (isBalanced, height)

        return dfs(root)[0]
