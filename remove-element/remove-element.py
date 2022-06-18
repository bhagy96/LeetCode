class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = nums.count(val)
        for _ in range(c):
            try:
                nums.remove(val)
            except:
                return nums
            