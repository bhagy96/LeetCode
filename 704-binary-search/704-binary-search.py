class Solution:
    
    # def search(self, nums, target):
    #     index = bisect.bisect_left(nums, target)
    #     return index if index < len(nums) and nums[index] == target else -1
    
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
    
    
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
            
    
#     def search(self, nums: List[int], target: int) -> int:
        
#         if len(nums)<=2:
#             # if target in nums:
#             try:
#                 return nums.index(target)
#             except:
#                 return -1
        
#         return self.binsearch(0, len(nums)-1, nums, target)
            