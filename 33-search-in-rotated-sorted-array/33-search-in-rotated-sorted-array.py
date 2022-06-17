
def check(arr, low, high, target):
        
        if low > high:
            return -1 
        
        mid = (low+high)//2
        
        if arr[mid] == target:
            return mid
        
        if arr[low] <= arr[mid]:
            
            if target>=arr[low] and target<=arr[mid]:
                return check(arr, low, mid-1, target)
            else:
                return check(arr, mid+1, high, target)
            
        if target>=arr[mid] and target<=arr[high]:
            return check(arr, mid+1, high, target)
        else:
            return check(arr, low, mid-1, target)
        
class Solution:
         
    def search(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        if (length==0):
            return -1
        if (length==1):
            if nums[0]!=target:
                return -1
            else:
                return 0
        
        out = check(nums, 0, length-1, target)
        print(out)
        if  out == -1:
            return -1
        else:
            return out
        
    
        
        
        