# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        stack = [(root,1)]
        dic = {1:[]}
        while stack:            
            node, d = stack.pop()
            if node:
                if d in dic.keys():
                    dic[d].append(node.val)
                else:
                    dic[d]  = [node.val]
                stack.extend([(node.right, d+1), (node.left,d+1)])                
        return dic.values()