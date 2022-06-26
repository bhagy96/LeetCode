class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict = collections.Counter(t)
        start = 0
        end = 0
        min_window = ""
        target_len = len(t)
        
        for end in range(len(s)):
            
			# If we see a target letter, decrease the total target letter count
            
            if target_dict[s[end]] > 0:
                # print("in decrease len", target_len)
                target_len -= 1
            target_dict[s[end]] -= 1
            # print(target_dict, target_len, s[end], end)
            while target_len==0:
                window_len = end - start + 1
                # print(window_len, s[start], start, s[end], end)
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = s[start : end + 1]
                    # print(min_window)
                
                target_dict[s[start]] += 1
                
                # above is to reinforce the below if condition.                
                # we increase the count because we have seen the variable,
                # now if its>0 then we know it'll appear in future as well
                # This is the reason we break out of the loop so that we know we are getting one more later
                # print('-----',target_dict)
                
                if target_dict[s[start]] > 0:
                    # print("inhere")
                    target_len += 1
                    
                start+=1
        
        
                
        return min_window