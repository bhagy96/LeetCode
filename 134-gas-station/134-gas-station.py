class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
            print(total_surplus, surplus)
        return -1 if (total_surplus < 0) else start
    
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
    