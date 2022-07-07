# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Iterative
    def invertTree(self, root):
        if not root:
            return root

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        return root
        
    
    #shorter
    
    # def invertTree(self, root):
    #     if root:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #         return root
    
#     def swap(self, node):
#         if node:
#             temp = node.left
#             node.left = node.right
#             node.right = temp
#         if node.left:
#             self.swap(node.left)
#         if node.right:
#             self.swap(node.right)
#         return node
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return root
            
#         return self.swap(root)