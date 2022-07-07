# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Recursive
    # def dfs(self, node, depth):
    #     if not node:
    #         return depth
    #     return max(self.dfs(node.left, depth+1), self.dfs(node.right, depth+1))
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     return self.dfs(root, 0)
    
    # Iterative
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        stack = [(root,1)]
        max_d = 0
        while stack:
            node, dep = stack.pop()
            if node:
                max_d = max(max_d, dep)
                stack.extend([(node.left, dep+1),(node.right, dep+1)])
        return max_d
    
    
        
    
        