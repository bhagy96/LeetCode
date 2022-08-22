class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
#         pl =len(part)
#         si, pi = 0,0
#         res = s
#         while si<len(s):
#             si = s.find(part,0,len(s))
#             if si==-1:
#                 return res
#             res = res[pi:si]
#             si = si + pl
#             pi = si
            
#         return s
        i = s.find(part)
        while(i!=-1):
            s = s[:i]+s[i+len(part):]
            i = s.find(part)
            # print(s)
        return s