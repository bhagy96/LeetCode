class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        f, s = 0,1
        for i in range(len(digits)-1, -1,-1):
            s += digits[i] 
            if s>=10:
                digits[i] = 0
                s = 1
                if i==0:
                    f = 1
            else:
                digits[i] = s
                return digits
        if f==1:
            digits.insert(0,1)
        return digits
                    