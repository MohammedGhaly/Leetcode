# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution1:    #works for any tree (not a binary search tree)
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         if root is None:
#             return (False, False)

#         left_result = self.lowestCommonAncestor(root.left, p, q)
#         right_result = self.lowestCommonAncestor(root.right, p, q)

#         if not isinstance(left_result, tuple):
#             return left_result
#         if not isinstance(right_result, tuple):
#             return right_result

#         root_result = (root == p or left_result[0] == True or right_result[0] == True,
#                        root == q or left_result[1] == True or right_result[1] == True)

#         if root_result[0] and root_result[1]:
#             return root
#         return root_result


class Solution:
    def between(self, num: int, n1: int, n2: int) -> bool:
        return (num >= n1 and num <= n2) or (num >= n2 and num <= n1)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if self.between(root.val, p.val, q.val):
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)


# n2 = TreeNode(2)
# n8 = TreeNode(8)
# n6 = TreeNode(6)

# n6.left = n2
# n6.right = n8

# sol = Solution()
# print(sol.lowestCommonAncestor(n6, n2, n8).val)
