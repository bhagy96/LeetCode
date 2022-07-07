class Solution:
    def binsearch(self, start, end, arr, target):
        
        
        mid = (start + end)//2
        if target==arr[mid]:
            return mid
        elif start>=end:
            return -1
        elif target<arr[mid]:
            return self.binsearch(start, mid, arr, target)
        elif target>arr[mid]:
            return self.binsearch(mid+1, end, arr, target)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # row = -1
        # for i in range(len(matrix)):
        #     if target==matrix[i][-1]:
        #         return True
        #     elif target<matrix[i][-1]:
        #         row = i
        #         break
        # if row==-1:
        #     return False
        for i in range(len(matrix)):
            if target>= matrix[i][0] and target<=matrix[i][-1]:
                # print('in')
                if self.binsearch(0, len(matrix[i]), matrix[i], target) != -1:
                    return True
        return False