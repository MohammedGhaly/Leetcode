# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left : TreeNode | None = left
        self.right : TreeNode | None= right
        
        
class Solution:
    def isSymmetric(self, root: TreeNode):
        if root is None: 
            return True
        left = root.left
        right = root.right
        
        def bfs(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if not (r.val == l.val):
                return False
            if not bfs(l.left, r.right):
                return False
            if not bfs(l.right, r.left):
                return False
            return True
        
        return bfs(left, right)
            

