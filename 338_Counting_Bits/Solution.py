from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if (n == 0):
            return [0]

        bitsCounted = [0, 1]
        accumulatorPointer = 0
        for i in range(2, n+1):
            if ((i & (i - 1)) == 0):
                accumulatorPointer = 0

            bitsCounted.append(bitsCounted[accumulatorPointer] + 1)
            accumulatorPointer += 1

        return bitsCounted

