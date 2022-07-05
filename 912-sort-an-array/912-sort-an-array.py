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
    
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.quicksort(0, len(nums)-1, nums)
#     def partition(self, l,r,nums):
#         ptr = l
#         for i in range(l,r):
#             # compare number at i and pivot
#             if nums[i]<=nums[r]:
#                 # swap numbers at i and ptr
#                 nums[i], nums[ptr] = nums[ptr], nums[i]
#                 ptr+=1
#         # swap numbers at ptr and pivot
#         nums[ptr], nums[r] = nums[r], nums[ptr]
#         return ptr
    
#     def quicksort(self, l, r, nums):
#         if len(nums)<=1:
#               return nums
#         mid = (l+r)//2
#         nums[mid], nums[r] = nums[r], nums[mid]
#         if l<r:
#             piv_ind = self.partition(l,r,nums)
#             self.quicksort(l, piv_ind-1, nums)
#             self.quicksort(piv_ind+1, r, nums)
#         return nums
        
    
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

    # ************************  Heap sort   ************************
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapsort(nums)
        return nums
    
    def heapify(self, nums, n, i): 
            l = 2 * i + 1
            r = 2 * i + 2
			
            largest = i
            # print('i,largest, l,r, n', i,largest, l,r, n)
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                
                self.heapify(nums, n, largest)
                
    def heapsort(self, nums):        
                
        n = len(nums) 

        for i in range(n//2-1, -1, -1): 
            # print(i)
            self.heapify(nums, n, i) 

        for i in range(n-1, 0, -1): 
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

    # Python program for implementation of heap Sort

# # To heapify subtree rooted at index i.
# # n is size of heap
# def heapify(arr, n, i):
# largest = i # Initialize largest as root
# l = 2 * i + 1 # left = 2*i + 1
# r = 2 * i + 2 # right = 2*i + 2

# # See if left child of root exists and is
# # greater than root
# if l < n and arr[i] < arr[l]:
# largest = l

# # See if right child of root exists and is
# # greater than root
# if r < n and arr[largest] < arr[r]:
# largest = r

# # Change root, if needed
# if largest != i:
# arr[i],arr[largest] = arr[largest],arr[i] # swap

# # Heapify the root.
# heapify(arr, n, largest)

# # The main function to sort an array of given size
# def heapSort(arr):
# n = len(arr)

# # Build a maxheap.
# # Since last parent will be at ((n//2)-1) we can start at that location.
# for i in range(n // 2 - 1, -1, -1):
# heapify(arr, n, i)

# # One by one extract elements
# for i in range(n-1, 0, -1):
# arr[i], arr[0] = arr[0], arr[i] # swap
# heapify(arr, i, 0)

# # Driver code to test above
# arr = [ 12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print ("Sorted array is")
# for i in range(n):
# print ("%d" %arr[i]),
# # This code is contributed by Mohit Kumra


        
            