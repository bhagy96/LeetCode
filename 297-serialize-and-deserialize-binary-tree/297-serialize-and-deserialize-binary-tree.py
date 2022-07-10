# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def preorder(self,node,pre_str):
        if node:
            pre_str += ',' + str(node.val)
            pre_str = self.preorder(node.left, pre_str)
            pre_str = self.preorder(node.right, pre_str)
        else:
            pre_str += ',' + 'n'
        return pre_str

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        pre_str = ''
        pre_str = self.preorder(root,pre_str)
        return  pre_str[1:]
    
    def build(self,preorder):
        if preorder:            
            val = preorder.pop(0)
            if val=='n':
                return None
            return TreeNode(int(val), self.build(preorder),self.build(preorder))
            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        preorder = [str(x) for x in data.split(',')] 
        return self.build(preorder)
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))