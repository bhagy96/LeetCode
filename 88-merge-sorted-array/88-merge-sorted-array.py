class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind = m+n-1
        m-=1
        n-=1
        
        while n>=0:
            if m>=0 and nums1[m]>nums2[n]:
                nums1[ind] = nums1[m]
                m-=1
            else:
                nums1[ind] = nums2[n]
                n-=1
            ind-=1
        