# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #Recursive
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        if not p and not q:
            return True
        else:
            return False
        # return p is q
    
    
    # Iterative
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #     elif not p or not q:
    #         return False
    #     stack = [(p,q)]
    #     while stack:
    #         (p,q) = stack.pop()
    #         if p and q and p.val==q.val:
    #             stack.extend([(p.left, q.left), (p.right, q.right)])
    #         elif p or q:
    #             return False
    #     return True