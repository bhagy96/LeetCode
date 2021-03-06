class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        re = []
        for s in strs:
            ss = "".join(sorted(s))
            if ss in dic.keys():
                dic[ss].append(s)
            else:
                dic[ss] = [s]
        return dic.values()