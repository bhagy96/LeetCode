class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        if l<=1:
            return nums
        mid = l//2
        l,r  = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])
        return self.merge(l,r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r
        ll = len(l) if len(l)<len(r) else len(r)
        i,j, newarr = 0,0,[]
        
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                newarr.append(l[i])
                i+=1
            else:
                newarr.append(r[j])
                j+=1
        return newarr + l[i:] + r[j:]
        
            