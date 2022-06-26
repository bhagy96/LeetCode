class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        def check_pali(st,l,r):
            while l>=0 and r<len(st) and st[l]==st[r]:
                l-=1
                r+=1
            return st[l+1:r]
            
            
        for i in range(len(s)):
            # for odd
            temps = check_pali(s,i,i)
            if len(temps) >len(ret):
                ret = temps
            temps = check_pali(s,i,i+1)
            if len(temps) >len(ret):
                ret = temps
        return ret