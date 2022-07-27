class Solution:
    def countSubstrings(self, s: str) -> int:
        # build the soln from  "longest palindrome substring" question
        global cnt
        cnt = 0        
        def checkpali(st,l,r):
            global cnt
            while l>=0 and r<len(st) and st[l]==st[r]:
                cnt+=1
                l-=1
                r+=1        
        for i in range(len(s)):
            checkpali(s,i,i)
            checkpali(s,i,i+1)            
        return cnt
            