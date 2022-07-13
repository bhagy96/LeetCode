class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution 1
        # nums = sorted(nums)
        # return nums[len(nums)-k]
        
        return heapq.nlargest(k, nums)[-1]