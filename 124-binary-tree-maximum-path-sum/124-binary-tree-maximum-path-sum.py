# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,node):
        if node:
            left_val = self.dfs(node.left)
            right_val = self.dfs(node.right)
            maxof3 = max(node.val, left_val+node.val, node.val+right_val)
            self.res = max(self.res, maxof3, left_val+ node.val+right_val)
            return maxof3
        else:
            return 0
        
            
            
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = float('-inf')
        self.dfs(root)
        return self.res