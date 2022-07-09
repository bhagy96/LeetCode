# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,lst):
        if not node: return
        self.inorder(node.left,lst)
        lst.append(node.val)
        self.inorder(node.right,lst)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.inorder(root,lst)
        return lst
    
        