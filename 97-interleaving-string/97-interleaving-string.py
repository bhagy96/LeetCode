class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m,n = len(s1), len(s2)
        if len(s3) != (m+n):
            return False   
        dp = [False for _ in range(n+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    dp[j] = True
                elif i==0:
                    dp[j] = dp[j-1] and (s2[j-1] == s3[i+j-1])
                elif j==0:
                    dp[j] = dp[j] and (s1[i-1] == s3[i+j-1])
                else:
                    dp[j] = (dp[j-1] and (s2[j-1] == s3[i+j-1])) or (dp[j] and (s1[i-1]==s3[i+j-1]))
                
        return dp[-1]
#         m,n = len(s1), len(s2)
#         if len(s3) != (m+n):
#             return False        
#         dp = [[False]* (n+1) for _ in range(m+1) ]
#         for i in range(m+1):
#             for j in range(n+1):
                
#                 if i==0 and j==0:
#                     dp[i][j] = True
#                 elif i==0:
#                     dp[i][j] = dp[i][j-1] and (s2[j-1] == s3[i+j-1])
#                 elif j==0:
#                     dp[i][j] = dp[i-1][j] and (s1[i-1] == s3[i+j-1])
#                 else:
#                     dp[i][j] = (dp[i][j-1] and (s2[j-1] == s3[i+j-1])) or (dp[i-1][j] and (s1[i-1]==s3[i+j-1]))
                
#         return dp[-1][-1]
    
        
                
            
            
            
    #     boolean dp[] = new boolean[s2.length() + 1];
    #     for (int i = 0; i <= s1.length(); i++) {
    #         for (int j = 0; j <= s2.length(); j++) {
    #             if (i == 0 && j == 0) {
    #                 dp[j] = true;
    #             } else if (i == 0) {
    #                 dp[j] = dp[j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1);
    #             } else if (j == 0) {
    #                 dp[j] = dp[j] && s1.charAt(i - 1) == s3.charAt(i + j - 1);
    #             } else {
    #                 dp[j] = (dp[j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) || (dp[j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1));
    #             }
    #         }
    #     }
    #     return dp[s2.length()];
    # }
            
    