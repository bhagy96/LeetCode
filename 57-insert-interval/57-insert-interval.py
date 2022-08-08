class Solution:
    def insert(self, inter: List[List[int]], ni: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(inter)):
            if ni[1]<inter[i][0]:
                res.append(ni)
                return res + inter[i:]
            elif ni[0]>inter[i][1]:
                res.append(inter[i])
            else:
                ni = [min(ni[0], inter[i][0]), max(ni[1], inter[i][1])]
        res.append(ni)
        return res
    