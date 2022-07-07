class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i,j = len(matrix)-1, 0
        while i>=0 and j<len(matrix[0]):
            if target==matrix[i][j]:
                return True
            elif target<matrix[i][j]:
                i-=1
            elif target>matrix[i][j]:
                j+=1
        return False
                
#     # O(mlogn)
#     def binsearch(self, start, end, arr, target):
#         mid = (start + end)//2
#         if target==arr[mid]:
#             return mid
#         elif start>=end:
#             return -1
#         elif target<arr[mid]:
#             return self.binsearch(start, mid, arr, target)
#         elif target>arr[mid]:
#             return self.binsearch(mid+1, end, arr, target)
    
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for i in range(len(matrix)):
#             if target>= matrix[i][0] and target<=matrix[i][-1]:
#                 if self.binsearch(0, len(matrix[i]), matrix[i], target) != -1:
#                     return True
#         return False