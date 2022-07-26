class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost)==2:
            return min(cost[0], cost[1])
        if len(cost)==3:
            return min(cost[0] + cost[1], cost[0] + cost[2], cost[1])
        cur, one, two = cost[-2], cost[-1], 0
        
        for i in range(len(cost)-3, -1, -1):
            two = one
            one = cur
            cur = cost[i] + min(one,two)
        return min(cur, one)