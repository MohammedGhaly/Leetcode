# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, mx: int) -> int:
            if node is None:
                return 0

            new_max = max(mx, node.val)
            return (node.val >= mx) + dfs(node.left, new_max) + dfs(node.right, new_max)

        if root is None:
            return 0

        return dfs(root, root.val)
