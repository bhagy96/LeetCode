class Solution:
    def isPali(self, s, l, r):
        # l, r = 0,len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    
    
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    
    
    # correct but the output's order not matching
#     def partition(self, s: str) -> List[List[str]]:
        
        
#         # res = [s[i: j] for i in range(len(s))
#         #   for j in range(i + 1, len(s) + 1)]
#         res = []
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 if self.isPali(s[i:j]):
#                     # print(list(s[:i]) , [s[i:j]] , list(s[j:]))
#                     part = list(s[:i]) + [s[i:j]] + list(s[j:])
#                     # print(part)
#                     if part not in res:
#                         res.append(part)
                
            
        
#         # printing result 
#         # print("All substrings of string are : " + str(res))
        
#         return res
    # return [["a","b","a","b"],["aba","b"],["a","bab"]]
    
    