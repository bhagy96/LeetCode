class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        s = format(n, 'b').zfill(32)
        for c in s:
            if c=='1': res+=1
        return res
        # print(s)