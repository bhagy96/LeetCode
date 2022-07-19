class Solution:
    
    
    
    
#     def dfs(self, r,c, grid):
#         if r not in range(self.rows) or c not in range(self.cols) or grid[r][c]==0 or (r,c) in self.visited:
#             return 0
#         self.visited.add((r,c))
#         self.area += 1
#         for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#             self.dfs(r+dr, c+dc, grid)
            
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         self.rows, self.cols = len(grid), len(grid[0])
#         maxa, self.area = 0, 0
#         self.visited = set()
#         islands = 0
        
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 self.area = 0
#                 if grid[r][c]==1 and (r,c) not in self.visited:
#                     self.dfs(r,c, grid)
#                     maxa = max(maxa,self.area)
#         return maxa


    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxa = 0
        global area
        area = 0
        visited = set()

        def dfs(r,c):
            global area
            if r not in range(rows) or c not in range(cols) or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            area += 1 
            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                dfs(r+dr, c+dc)            

        for r in range(rows):
            for c in range(cols):
                area = 0
                if grid[r][c]==1 and (r,c) not in visited:
                    dfs(r,c)
                    maxa = max(maxa,area)
        return maxa
                    