class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]* (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (len(s) - i >= len(w)) and s[i : i+len(w)] == w: # if the lenghth and word matches
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
        