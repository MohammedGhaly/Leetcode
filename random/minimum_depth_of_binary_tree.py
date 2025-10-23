# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node.left is None and node.right is None:
                return 0
            
            left = 10**5
            right = 10**5
            
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            
            return min(left+1, right+1)
        
        return dfs(root) + 1


