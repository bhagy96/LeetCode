# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def issameTree(self,p,q):
        if p and q:
            return p.val==q.val and self.issameTree(p.left,q.left) and self.issameTree(p.right,q.right)
        if not p and not q:
            return True
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val==subRoot.val and self.issameTree(node, subRoot):
                    return True
                else:
                    stack.extend([node.left, node.right])
                
        return False