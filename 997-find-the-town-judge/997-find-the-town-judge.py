class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and not trust: return 1
        if len(trust)<n-1: return -1
        d = {}
        f = []
        for i in range(len(trust)):
            if trust[i][1] not in d.keys():
                d[trust[i][1]] = [trust[i][0]]
            else:
                d[trust[i][1]].append(trust[i][0])
            f.append(trust[i][0])
        for k,v in d.items():
            if len(v)==n-1 :
                if k not in f:
                    return k
        return -1