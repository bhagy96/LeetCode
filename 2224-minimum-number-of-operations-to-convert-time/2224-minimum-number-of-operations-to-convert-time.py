class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        time = [60,15,5,1] 
        inlst = current.split(':')
        outlst = correct.split(':')
        re = 0
        rem_time = (int(outlst[0]) - int(inlst[0]))*60 +  (int(outlst[1]) - int(inlst[1]))
        for t in time:
            if t<=rem_time:
                while rem_time>-1:
                    rem_time -= t
                    re+=1
                    if rem_time==0: return re
                rem_time += t
                re-=1
        return re