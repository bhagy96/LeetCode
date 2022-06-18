class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for n in nums:
            c = nums.count(n)
            if c > 1:
                for _ in range(c-1):
                    nums.remove(n)
        return len(nums)
            