# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        def dfs(node:TreeNode):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res