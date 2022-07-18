class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image),len(image[0])
        if image[sr][sc]==color: return image
        ogcolor = image[sr][sc]
        visited = set()
        # marked = [[False for j in range(cols)] for i in range(rows)]
        
        def bfs(r,c):
            q = collections.deque()
            # visited.add((r,c))
            q.append((r,c))
            while q:
                r,c = q.popleft()
                if (r,c) not in visited:
                # if not marked[r][c]:
                    visited.add((r,c))
                    image[r][c] = color
                    # marked[r][c] = True
                    for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                        nr,nc = r+dr, c+dc
                        if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and image[nr][nc]==ogcolor:
                                q.append((nr,nc))
            
            
        bfs(sr,sc)
        return image
    
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
        
        