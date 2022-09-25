import math
from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.arr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self._insertValueOnArray(val)

    def _insertValueOnArray(self, val) -> None:
        leftBound = 0
        rightBound = len(self.arr)
        while leftBound < rightBound:
            middleElement = math.floor((leftBound + rightBound) / 2)
            if (val > self.arr[middleElement]):
                leftBound = middleElement + 1
            else:
                rightBound = middleElement
        self.arr.insert(rightBound, val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.arr.remove(val)

    def top(self) -> int:
        val = self.stack.pop()
        self.stack.append(val)
        return val

    def getMin(self) -> int:
        return self.arr[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
