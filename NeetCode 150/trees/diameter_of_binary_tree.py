# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0
        self.dfs(root)
        return self.max_diameter

    def dfs(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.max_diameter = max(left + right, self.max_diameter)
        return max(left, right) + 1


lr = TreeNode(5)
ll = TreeNode(4)
r = TreeNode(3)
l = TreeNode(2, ll, lr)
root = TreeNode(1, l, r)

sol = Solution()
print(sol.diameterOfBinaryTree(root))
