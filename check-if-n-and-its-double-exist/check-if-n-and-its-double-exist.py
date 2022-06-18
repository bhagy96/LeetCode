class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        narr = []
        for n in arr:
            if n!=0:
                narr.append(n*2)
        for n in narr:
            if n in arr:
                return True