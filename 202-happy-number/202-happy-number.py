class Solution:
    def isHappy(self, n: int) -> bool:
        sqs = sum([ int(i)*int(i) for i in str(n) ])
        if sqs == 1:
            return True
        elif sqs>9 or sqs==7:
            return self.isHappy(sqs)
        else:
            return False