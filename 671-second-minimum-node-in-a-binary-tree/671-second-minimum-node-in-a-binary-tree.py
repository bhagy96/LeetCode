# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root: return
        stack = [root]
        minv, sec_minv = float('inf'),float('inf')
        while stack:
            node = stack.pop()
            if node:
                print(node.val , minv, sec_minv)
                if node.val<minv:
                    sec_min = minv
                    minv = node.val                    
                elif node.val!=minv and node.val<sec_minv:
                    sec_minv = node.val         
                stack.extend([node.left, node.right])
        if sec_minv==float('inf'):
            return -1
        return sec_minv
                
        