class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]

        while start >= end:
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
            if start == end:
                return start
            total += gas[end] - cost[end]
            end += 1
        return -1
    
#         i = 0
#         while i<len(gas):
#             j, cnt, cumcost, flag = i, 0, 0, 0
#             while cnt<len(gas):
#                 cumcost += gas[j]-cost[j]
#                 if cumcost<0:
#                     flag = 1
#                     break
#                 j+=1
#                 if j==len(gas):
#                     j = 0
#                 cnt+=1
#             if cnt==len(gas):
#                 return i
#             if flag==1 and i>j:
#                 return -1
#             i = j+1
                
#         return -1
    