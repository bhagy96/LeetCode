class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        if l<3:
            return False
        flag,i,j = -1,0,1
        while j!=(l):
            if arr[i]==arr[j]:
                return False
            if flag==-1:
                if arr[i]<arr[j]:
                    flag = 0
                else:
                    return False
            if flag==0 and arr[i]>arr[j]:
                flag = 1
            elif flag==1 and arr[i]<arr[j]:
                return False
            i+=1
            j+=1
        if flag==-1 or flag==0:
            return False
        return True
            
            