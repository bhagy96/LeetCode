class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for pt in points:
            heapq.heappush(min_heap,(pt[0]*pt[0] +pt[1]*pt[1], pt))
        res = []
        while k!=0:
            _, pt = heapq.heappop(min_heap)
            res.append(pt)
            k-=1
        return res
            