# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def swap(self, node):
        if node:
            temp = node.left
            node.left = node.right
            node.right = temp
        if node.left:
            self.swap(node.left)
        if node.right:
            self.swap(node.right)
        return node
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
            
        return self.swap(root)