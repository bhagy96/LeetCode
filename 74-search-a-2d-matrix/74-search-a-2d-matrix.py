class Solution:
    
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     r = bisect_left(matrix, target, key=lambda row: row[-1])  # or key=itemgetter(-1)
    #     print(r)
    #     return r < len(matrix) and matrix[r][bisect_left(matrix[r], target)] == target
    
    
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
        
        row = -1
        # print(len(matrix))
        for i in range(len(matrix)):
            # print('in')
            if target==matrix[i][-1]:
                return True
            elif target<matrix[i][-1]:
                row = i
                break
        # print(row)
        if row==-1:
            return False
        if self.binsearch(0, len(matrix[row]), matrix[row], target) == -1:
            return False
        else:
            return True
            
        