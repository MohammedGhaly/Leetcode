# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not len(inorder):
            return None

        parent = None

        for item in preorder:
            if item in inorder:
                parent = item
                break

        left = self.buildTree([num for num in preorder if not num == parent],
                              inorder[0: inorder.index(parent)])  # left
        right = self.buildTree([num for num in preorder if not num == parent],
                               inorder[inorder.index(parent) + 1:])  # right

        return TreeNode(parent, left, right)


# n7 = TreeNode(7)
# n15 = TreeNode(15)
# n20 = TreeNode(20, n15, n7)
# n9 = TreeNode(0)
# n3 = TreeNode(3, n9, n20)


print(Solution().buildTree([3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
