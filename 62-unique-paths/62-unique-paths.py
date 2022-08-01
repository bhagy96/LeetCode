class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1: return 1
        row = [1]*(n)
        row.append(0)
        for i in range(m-2, -1, -1):
            newrow = [0]*(n+1)
            for j in range(n-1, -1, -1):
                newrow[j]  = row[j] + newrow[j+1]
            row = newrow
        
        return newrow[0]