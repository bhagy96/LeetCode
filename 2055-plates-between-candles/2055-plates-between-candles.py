class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        

        n=len(s)
        
        prefcandle=[-1]*n #closest left candles
        ind =-1
        for i in range(n):
            if s[i] == '|':
                ind=i
            prefcandle[i]=ind
            
        suffcandle=[0]*n #closest right candles
        ind = float('inf')       
        for i in range(n-1, -1, -1):
            if s[i]=='|':
                ind=i
            suffcandle[i]=ind
        
        pref=[0]*n #number of plates  till ith position        
        ind=-1
        c=0
        for i in range(n):
            if ind!=-1 and s[i]=='*':
                c+=1
            elif s[i]=='|':
                ind=i
            pref[i]=c
        # print(prefcandle, suffcandle, pref)
            
        m=len(queries)
        ans=[0]*m

        for i in range(m):
            c=0
            l=queries[i][0]
            r=queries[i][1]
            if prefcandle[r]<l or suffcandle[l]>r:
                continue
            ans[i]=pref[prefcandle[r]]-pref[suffcandle[l]]
        return ans
    
    
    
    
    # Tle Solutions
    
#         ans = []
#         f_in = s.find('|')
#         can_ind = [f_in]
#         count = [0]
#         temp_c = 0
#         for i in range(f_in+1,len(s)):            
#             if s[i]=='|':
                
#                 can_ind.append(i)
#                 count.append(temp_c)
#                 temp_c = 0
#             if s[i]=='*':
#                 temp_c += 1
        
#         for q in queries:
#             sub_str = s[q[0]:q[1]+1]
#             first_ind, last_ind = sub_str.find('|'), sub_str.rfind('|')
#             if last_ind == -1 or first_ind == last_ind:
#                 ans.append(0)
#             else:
#                 fc = 0
#                 first_ind += q[0]
#                 last_ind += q[0]                 
#                 st, en = can_ind.index(first_ind)+1, can_ind.index(last_ind)+1
#                 ans.append(sum(count[st:en]))
#         return ans
        
        
#         ans = []
#         for q in queries:
#             count, temp_c = 0,0
#             first = 0
#             sub_str = s[q[0]:q[1]+1]
            
#             f_in = sub_str.find('|')
#             # print(sub_str[f_in+1:])
#             for c in sub_str[f_in:]:
#                 # print(c, first)
#                 if c=='*':
#                     if first == 0:
#                         # print('in 1')
#                         continue
#                     else:
#                         temp_c += 1
#                 elif c == '|':
#                     # print('in 3')
#                     first = 1
#                     count += temp_c
#                     temp_c = 0
#             ans.append(count)
#         return ans
                    
        
            
        # ans = []
        # for q in queries:
        #     stack = []
        #     sub_str = s[q[0]:q[1]+1]
        #     first_ind, last_ind = sub_str.find('|'), sub_str.rfind('|')
        #     if last_ind == -1 or first_ind == last_ind:
        #         ans.append(0)
        #     else:
        #         new_sub = sub_str[first_ind : last_ind+1]
        #         ans.append(new_sub.count('*'))
        # return ans
            
                