class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        if l % groupSize != 0:
            return False
        if groupSize==1: return True
        dic = defaultdict(int)
        for h in hand:
            dic[h] += 1
        heapify(hand)
        
        for i in range(l//groupSize):
            start = heappop(hand)
            while dic[start]==0:
                start = heappop(hand)
            for i in range(groupSize):
                dic[start] -= 1
                if dic[start] < 0:
                    return False
                start += 1
        return True