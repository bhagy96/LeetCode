class Solution:
    
    def binsearch(self, start, end, arr, target):
        
        
        mid = (start + end)//2
        # print('start, end, mid ', start, end, mid)
        if target==arr[mid]:
            return mid
        elif start>=end:
            return -1
        elif target<arr[mid]:
            return self.binsearch(start, mid, arr, target)
        elif target>arr[mid]:
            return self.binsearch(mid+1, end, arr, target)
            
    
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums)<=2:
            # if target in nums:
            try:
                return nums.index(target)
            except:
                return -1
        
        return self.binsearch(0, len(nums)-1, nums, target)
            