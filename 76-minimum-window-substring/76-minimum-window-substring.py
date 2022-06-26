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
                    
				# Increase the letter count of the current letter
                target_dict[s[start]] += 1
                # print('-----',target_dict)
                
				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_dict[s[start]] > 0:
                    # print("inhere")
                    target_len += 1
                    
                start+=1
        
        
                
        return min_window