class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n1,n2 = edges[0]
        n3, n4 = edges[1]
        if n1==n3:
            return n1
        if n1==n4:
            return n1
        return n2