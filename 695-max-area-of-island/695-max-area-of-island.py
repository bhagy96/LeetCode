class Solution:
    
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         if not grid or not grid[0]: return 0
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islands = 0
#         def dfs(r,c):
#             if r not in range(rows) or c not in range(cols) or grid[r][c]==0 or (r,c) in visited:
#                 return
#             visited.add((r,c))
#             for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#                 dfs(r+dr,c+dc)
        
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]==1 and (r,c) not in visited:
#                     islands += 1
#                     dfs(r,c)
                    
#         return islands
    
    
    
    def dfs(self, r,c, grid):
        if r not in range(self.rows) or c not in range(self.cols) or grid[r][c]==0 or (r,c) in self.visited:
            return 0
        self.visited.add((r,c))
        self.area += 1
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            self.dfs(r+dr, c+dc, grid) 
            # self.dfs(r+dr, c+dc, grid) 
            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        maxa, self.area = 0, 0
        self.visited = set()
        islands = 0
        
        for r in range(self.rows):
            for c in range(self.cols):
                self.area = 0
                if grid[r][c]==1 and (r,c) not in self.visited:
                    # islands+=1
                    # self.dfs(r, c, grid) 
                    self.dfs(r,c, grid)
                    # print(self.area)
                    maxa = max(maxa,self.area)
                    
                    
        # print(islands)
        return maxa
                    
        
        
        
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         maxa, area = 0, 0
#         visited = set()
        
#         def dfs(r,c):
#             if r not in range(rows) or c not in range(cols) or grid[r][c]=="0" or grid[r][c] in visited:
#                 return 0
#             visited.add((r,c))
#             for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#                 area += dfs(r+dr, c+dc)            
            
#         for r in range(rows):
#             for c in range(cols):
#                 area = 0
#                 if grid[r][c]==1 and (r,c) not in visited:
#                     area = dfs(r,c)
#                     maxa = max(maxa,area)
                    
#                     # islands+=1
#         return maxa
                    