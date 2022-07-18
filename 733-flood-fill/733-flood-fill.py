class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image),len(image[0])
        if image[sr][sc]==color: return image
        ogcolor = image[sr][sc]
        visited = set()
        marked = [[False for j in range(cols)] for i in range(rows)]
        # print(marked)
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()
                # visited.add((r,c))
                # print(r,c)
                if not marked[r][c]:
                    image[r][c] = color
                    marked[r][c] = True
                    for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                        nr,nc = r+dr, c+dc
                        # print('infor',nr,nc)
                        if nr in range(rows) and nc in range(cols):
                            if not marked[nr][nc] and image[nr][nc]==ogcolor:
                                # print('add', nr,nc)
                                q.append((nr,nc))
            
            
        bfs(sr,sc)
        return image
        
        