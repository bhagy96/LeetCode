class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if r in range(rows) and c in range(cols) and grid[r][c]==1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
    
    
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         # return 0
#         # print(grid)
#         if not grid: return 0
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         global time
#         time = 0
#         def bfs(r,c):
#             global time
#             flag1 = 0
#             q = collections.deque()
#             q.append((r,c))
#             # print(r,c)
#             while q:
                
#                 qsize = len(q)
#                 # print("queue , size ", q, len(q))
                
#                 while qsize!=0:
#                     row,col = q.popleft()                
                
#                     if grid[row][col]==2 and (row,col) not in visited:  
#                         # print('row,col, time', row,col, time)
#                         visited.add((r,c))
#                         flag = 1
#                         for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#                             r, c = row+dr, col+dc
#                             if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited:
#                                 # print("in if ", r, c)
#                                 flag1 = 1
#                                 # if flag:
#                                 #     # time +=1
#                                 #     flag = 0
#                                 #     print('time ',time)
#                                 grid[r][c] = 2
#                                 q.append((r,c))
#                                 # visited.add((r,c))
#                     qsize -= 1
                    
#                 if flag1:
#                     time+=1
#                     flag1=0
        
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c]==2 and (r,c) not in visited:
#                     # print(r,c)
#                     bfs(r,c)
#                     # islands += 1
#         # print(grid)
#         # print('*************')
#         if any(1 in row for row in grid): return -1
#         # if 1 in grid:
#         #     return -1
#         # if flag1==0:
#         #     return 0
#         return time