# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
        
#         def valid(node, left, right):
#             if not node:
#                 return True
#             if node.val <= left or node.val >= right:
#                 return False
            
#             return (valid(node.left, left, node.val) and
#                     valid(node.right, node.val, right))
        
#         return valid(root, float("-inf"), float("inf"))
    
    def inorder(self,node, lst):
        if not node: return
        self.inorder(node.left, lst)
        lst.append(node.val)
        self.inorder(node.right, lst)
    def isValidBST(self, root: TreeNode) -> bool:
        
        lst = []
        self.inorder(root,lst)
        for i in range(1,len(lst)):
            if lst[i-1]>=lst[i]:
                return False
        return True
        
        