class Solution:
    def countSubstrings(self, s: str) -> int:
        global cnt
        cnt = 0
        def checkpali(st,l,r):
            global cnt
            while l>=0 and r<len(st) and st[l]==st[r]:
                cnt+=1
                l-=1
                r+=1
            print(st[l+1:r],l+1,r)
            return st[l+1:r]
        
        for i in range(len(s)):
            checkpali(s,i,i)
            checkpali(s,i,i+1)
            
        return cnt
            