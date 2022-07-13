class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        stones = [-1*s for s in stones]
        
        heapq.heapify(stones)
        # print(stones)
        while len(stones)>1:
            
            lar = -1*heapq.heappop(stones)
            seclar = -1*heapq.heappop(stones)
            if seclar<lar:
                stones.append(-1*(lar-seclar))
                heapq.heapify(stones)
        if stones:
            if stones[0]<0:
                return -1*stones[0]
            return stones[0]
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
            