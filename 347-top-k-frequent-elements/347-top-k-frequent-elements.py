class Solution:
    def topKFrequent(self, nums: List[int], l: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n]+=1
        dic = {k:v for k,v in sorted(dic.items(), key = lambda item:item[1], reverse = True)}
        return list(dic.keys())[:l]
#         for k,v in dic.items():
#             if l==0: return res
#             res.append()
            
            