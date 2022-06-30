class MyCircularQueue:

    def __init__(self, k: int):
        self.lst = [-1 for _ in range(k)]
        self.len = k
        self.top = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.top += 1
            self.lst[self.top] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.lst.pop(0)
            self.top -= 1
            self.lst.append(-1)
            return True

    def Front(self) -> int:
        return self.lst[0]

    def Rear(self) -> int:
        return self.lst[self.top]

    def isEmpty(self) -> bool:
        if self.lst[0] == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.lst[-1] == -1:
            return False 
        else:
            return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()