class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        length = len(s)
        mid = length//2
        if length==1: return True
        mid
        if length%2==0: 
            l,r = mid-1, mid
        else:
            l,r = mid,mid
        # print(length,l,r,s)
        while l>=0 and r<length:
            if s[l]!=s[r]:
                return False
            l -= 1
            r += 1
            
        return True