class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        tempc, maxc = 0,0
        temps = ''
        for c in s:
            if c in temps:
                if tempc>maxc:
                    maxc = tempc 
                temps = temps[temps.index(c)+1:] +c
                tempc = len(temps)         
            else:
                tempc+=1
                temps += c
        if tempc>maxc:
            return tempc
        return maxc