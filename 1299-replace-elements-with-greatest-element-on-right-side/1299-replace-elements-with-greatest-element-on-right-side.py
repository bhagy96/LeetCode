class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        L = len(arr) 
        if L<2:
            return [-1]
        i = L-1
        j = i-1
        while i!=1:
            if arr[j]<arr[i]:
                arr[j] = arr[i]
            j-=1
            i-=1
        arr.pop(0)
        arr.append(-1)
        return arr
    
        # L = len(arr)        
        # for i in range(L-1):
        #     arr[i] = max(arr[i+1:L])
        # arr[-1] = -1
        # return arr