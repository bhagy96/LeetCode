class MedianFinder:

    def __init__(self):
        
        self.arr, self.min_heap, self.max_heap = [], [], []
        self.len = 0

    def addNum(self, num: int) -> None:
        
        if self.len==0:
            heapq.heappush(self.max_heap, -num)            
        elif num < -self.max_heap[0]:
            if len(self.max_heap)<=len(self.min_heap):
                heapq.heappush(self.max_heap, -num)
            else:
                top = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -top)
                heapq.heappush(self.max_heap, -num)
        elif not self.min_heap:
            heapq.heappush(self.min_heap, num)
        elif num > self.min_heap[0]:
            if len(self.min_heap)<=len(self.max_heap):
                heapq.heappush(self.min_heap, num)
            else:
                top = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -top)
                heapq.heappush(self.min_heap, num)
        elif len(self.max_heap)<=len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.len+=1


    def findMedian(self) -> float:
        if len(self.max_heap)==len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2.0
        elif len(self.max_heap)<len(self.min_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()