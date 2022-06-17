class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # arr.insert(1,3)
        # arr.pop()
        # print(arr)
        i=0
        while i<(len(arr)):#for i in range(len(arr)):
            # print(i)
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i+=1
            i+=1
        # print(arr)