class Solution:
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color: return image
        rows, cols = len(image),len(image[0])        
        ogcolor = image[sr][sc]
        visited = set()
        
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or image[r][c]!=ogcolor:
                return
            visited.add((r,c))
            image[r][c] = color
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                dfs(r+dr, c+dc)
                
                        
            # q = collections.deque()
            # q.append((r,c))
            # while q:
            #     r,c = q.popleft()
            #     if (r,c) not in visited:
            #         visited.add((r,c))
            #         image[r][c] = color
            #         for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            #             nr,nc = r+dr, c+dc
            #             if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and image[nr][nc]==ogcolor:
            #                     q.append((nr,nc))
            
            
        dfs(sr,sc)
        return image
    
    
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         rows, cols = len(image),len(image[0])
#         if image[sr][sc]==color: return image
#         ogcolor = image[sr][sc]
#         visited = set()
        
#         def bfs(r,c):
#             q = collections.deque()
#             q.append((r,c))
#             while q:
#                 r,c = q.popleft()
#                 if (r,c) not in visited:
#                     visited.add((r,c))
#                     image[r][c] = color
#                     for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#                         nr,nc = r+dr, c+dc
#                         if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and image[nr][nc]==ogcolor:
#                                 q.append((nr,nc))
            
            
#         bfs(sr,sc)
#         return image
    
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         rows, cols = len(image),len(image[0])
#         if image[sr][sc]==color: return image
#         ogcolor = image[sr][sc]
#         visited = set()
#         marked = [[False for j in range(cols)] for i in range(rows)]
#         def bfs(r,c):
#             q = collections.deque()
#             q.append((r,c))
#             while q:
#                 r,c = q.popleft()
#                 if not marked[r][c]:
#                     image[r][c] = color
#                     marked[r][c] = True
#                     for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#                         nr,nc = r+dr, c+dc
#                         if nr in range(rows) and nc in range(cols):
#                             if not marked[nr][nc] and image[nr][nc]==ogcolor:
#                                 q.append((nr,nc))
            
            
#         bfs(sr,sc)
#         return image
        
        