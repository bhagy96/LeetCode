class Solution:   
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pac, atla = set(),set()
        ret = []
        def dfs(r,c, visited, prevheight):
            if (r,c) in visited or r<0 or c<0 or r==rows or c==cols:
                return
            if  heights[r][c]<prevheight:
                return
            visited.add((r,c))
            for dr,dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                dfs(r+dr, c+dc, visited, heights[r][c])
            
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atla, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atla, heights[r][cols-1])
        
        return pac.intersection(atla)