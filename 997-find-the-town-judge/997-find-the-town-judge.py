class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and not trust: return 1
        d = {}
        f = []
        for i in range(len(trust)):
            if trust[i][1] not in d.keys():
                d[trust[i][1]] = [trust[i][0]]
            else:
                d[trust[i][1]].append(trust[i][0])
            f.append(trust[i][0])
        # print('**********')
        
        # print(d, d.values())
        for k,v in d.items():
            # print(k,v)
            if len(v)==n-1 :
                if k not in f:
                    # print('in')
                    return k
        return -1
#         if not trust:
#             if n==1: return 1
#             return -1
#         elif len(trust)>=n: return -1
#         elif len(trust)==1:
#             return trust[0][1]
#         tj, first = trust[0][1], [trust[0][0]]
#         for i in range(1,len(trust)):
#             if trust[i][0] == tj : return -1
#             if trust[i][0] in first: return -1
#             first.append(trust[i][0])
#         return tj
            
        