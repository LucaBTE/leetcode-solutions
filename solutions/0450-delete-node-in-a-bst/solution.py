# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        
        if root is None:
            return None
        
        # They key is lower than the current node value,
        # So we look for that value recursively into its root.left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # key > current node value, we look into its right subtree!
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # key == root.val ! We found the node to remove!
        else:
            
            # Case 1: No left son
            if root.left is None:
                return root.right
            
            # Case 2: No right son
            if root.right is None:
                return root.left
            
            # Case 3: Two sons
            successor = root.right

            while successor.left is not None:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root



