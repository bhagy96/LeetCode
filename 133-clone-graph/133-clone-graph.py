"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        dic = {node: Node(node.val, [])}
        stack = [node]
        while stack:
            cur_node = stack.pop()
            for nei in cur_node.neighbors:
                if nei not in dic:
                    dic[nei] = Node(nei.val,[])
                    stack.append(nei)
                dic[cur_node].neighbors.append(dic[nei])
        
        
        return dic[node]
        