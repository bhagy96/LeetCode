class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i,L = 0,len(arr)
        while i<L:
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i+=1
            i+=1