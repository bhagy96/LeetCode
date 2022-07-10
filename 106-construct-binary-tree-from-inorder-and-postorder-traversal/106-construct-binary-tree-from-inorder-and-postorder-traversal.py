# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            curr_val = postorder.pop()
            ind = inorder.index(curr_val)
            node = TreeNode(curr_val)
            node.right = self.buildTree(inorder[ind+1:],postorder)
            node.left =  self.buildTree(inorder[:ind],postorder)
            return node