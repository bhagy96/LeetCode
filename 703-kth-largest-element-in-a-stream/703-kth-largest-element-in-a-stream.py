class KthLargest:
    
    # Its creating a min heap so that kth largest stays at the top
    

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
    

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# Heap implemented from scratch
# def max_heapify(arr, n, i):
#     largest_pos = i
#     left_pos = 2*i +1
#     right_pos = 2*i +2

#     if left_pos<n and arr[largest_pos]<arr[left_pos]: #invert 2nd cond sign for min heap
#         largest_pos = left_pos
#     if right_pos<n and arr[largest_pos]<arr[right_pos]:#invert 2nd cond sign for min heap
#         largest_pos = right_pos
#     if largest_pos!=i:
#         arr[i], arr[largest_pos] = arr[largest_pos], arr[i]
#         max_heapify(arr, n, largest_pos)



# arr = [2,66,30,5,9,10]
# n = len(arr)

# for i in range(n//2 - 1, -1,-1):
#     min_heapify(arr, n, i)
#   # max_heapify(arr, n, i)
# print(arr)