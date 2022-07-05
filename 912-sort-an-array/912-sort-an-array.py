class Solution:
    
    # ************************  Merge Sort ************************
    
#     def sortArray(self, nums: List[int]) -> List[int]:
        
#         l = len(nums)
#         if l<=1:
#             return nums
#         mid = l//2
#         l,r  = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])
#         return self.merge(l,r)
    
#     def merge(self, l, r):
#         if not l or not r:
#             return l or r
#         ll = len(l) if len(l)<len(r) else len(r)
#         i,j, newarr = 0,0,[]
        
#         while i<len(l) and j<len(r):
#             if l[i]<r[j]:
#                 newarr.append(l[i])
#                 i+=1
#             else:
#                 newarr.append(r[j])
#                 j+=1
#         return newarr + l[i:] + r[j:]
    
    # ************************  Quick sort   ************************
    
    # Runtime: O(nlogn) expected, O(n^2) worst case.
    # Space complexity O(1)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(0, len(nums)-1, nums)
    def partition(self, l,r,nums):
        ptr = l
        for i in range(l,r):
            # compare number at i and pivot
            if nums[i]<=nums[r]:
                # swap numbers at i and ptr
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr+=1
        # swap numbers at ptr and pivot
        nums[ptr], nums[r] = nums[r], nums[ptr]
        return ptr
    
    def quicksort(self, l, r, nums):
        if len(nums)<=1:
              return nums
        mid = (l+r)//2
        nums[mid], nums[r] = nums[r], nums[mid]
        if l<r:
            piv_ind = self.partition(l,r,nums)
            self.quicksort(l, piv_ind-1, nums)
            self.quicksort(piv_ind+1, r, nums)
        return nums
        
    
    # Divide and Conquer
    # Runtime: O(nlogn) expected, O(n^2) worst case.
    # With a proper choice of pivot (using the median of medians algorithm), the runtime can          be reduced to strict O(nlogn).
    # Space: O(n) expected, O(n^2) worst case
    
#     if len(nums) <= 1:
#         return nums

#     pivot = random.choice(nums)
#     lt = [v for v in nums if v < pivot]
#     eq = [v for v in nums if v == pivot]
#     gt = [v for v in nums if v > pivot]

#     return self.quicksort(lt) + eq + self.quicksort(gt)

        
            