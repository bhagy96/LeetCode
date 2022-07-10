# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        if not root: return ''
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
                
        while result[-1] == 'null':
            result.pop()
        # print(result)
            
        return ','.join(result)
        

    def deserialize(self, data):
        # print('here' , data.split())
        return TreeNode(data.split()[0]) if data else None
    
#     def preorder(self,node,pre_str):
#         if node:
#             pre_str += ',' + str(node.val)
#             pre_str = self.preorder(node.left, pre_str)
#             pre_str = self.preorder(node.right, pre_str)
#         else:
#             pre_str += ',' + 'n'
#         return pre_str

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root: return ''
#         pre_str = ''
#         pre_str = self.preorder(root,pre_str)
#         return  pre_str[1:]
    
#     def build(self,preorder):
#         if preorder:            
#             val = preorder.pop(0)
#             if val=='n':
#                 return None
#             return TreeNode(int(val), self.build(preorder),self.build(preorder))
            
        
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         print(data)
#         if not data: return None
#         preorder = [x for x in data.split(',')] 
#         return self.build(preorder)
#         # return TreeNode(data.split()[0]) if data else None
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))