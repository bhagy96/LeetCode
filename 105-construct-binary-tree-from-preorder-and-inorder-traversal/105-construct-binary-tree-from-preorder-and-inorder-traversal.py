# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:            
            curr_val = preorder.pop(0)
            ind = inorder.index(curr_val)
            return TreeNode(curr_val, self.buildTree(preorder, inorder[:ind]), self.buildTree(preorder, inorder[ind+1:]))