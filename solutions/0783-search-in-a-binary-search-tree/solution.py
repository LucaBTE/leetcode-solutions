# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        node = root

        while node is not None:
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                return node
