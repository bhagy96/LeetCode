# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # More Efficient
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        print(map_inorder)
        def recur(low, high):
            if low > high: return None
            x = TreeNode(postorder.pop())
            # print('x', x)
            mid = map_inorder[x.val]
            print('m', mid)
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)
    
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if inorder:
#             curr_val = postorder.pop()
#             ind = inorder.index(curr_val)   # Takes O(n) here
#             node = TreeNode(curr_val)
#             node.right = self.buildTree(inorder[ind+1:],postorder) # Extra stack calls
#             node.left =  self.buildTree(inorder[:ind],postorder)    # Extra stack calls
#             return node