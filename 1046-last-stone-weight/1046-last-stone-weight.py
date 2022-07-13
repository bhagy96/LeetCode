class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones: return 0
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, -s)
            
        while len(max_heap)>1:            
            lar = -1*heapq.heappop(max_heap)
            seclar = -1*heapq.heappop(max_heap)
            if seclar<lar:
                heapq.heappush(max_heap, -1*(lar-seclar))
        if max_heap:
            if max_heap[0]<0:
                return -1*max_heap[0]
            return max_heap[0]
        return 0
            
        
        
        
        
        
        # stones = sorted(stones)
        # while len(stones)>1:
        #     if stones[-1]==stones[-2]:
        #         stones.pop()
        #         stones.pop()
        #     else:
        #         stones[-2] = stones[-1] - stones[-2]
        #         stones.pop()
        # 
            