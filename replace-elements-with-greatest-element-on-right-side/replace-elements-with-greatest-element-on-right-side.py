class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        L = len(arr)        
        for i in range(L-1):
            arr[i] = max(arr[i+1:L])
        arr[-1] = -1
        return arr