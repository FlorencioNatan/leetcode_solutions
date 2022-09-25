from typing import List, Tuple
from collections import deque
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFrequency = self._create_nums_frenquecy_array(nums)
        if (k < len(numsFrequency)):
            self._quickselect(0, len(numsFrequency) - 1, k, numsFrequency)
        return self._build_result_array(numsFrequency, k)

    def _create_nums_frenquecy_array(self, nums: List[int]) -> List[Tuple[int, int]]:
        numsFrequency = dict()
        for i in nums:
            if (i not in numsFrequency):
                numsFrequency[i] = 1
            else:
                numsFrequency[i] += 1
        return list(numsFrequency.items())

    def _quickselect(self, begin: int, end: int, k: int, tuples: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        stack = deque()
        stack.append((begin, end))
        while len(stack) > 0:
            begin, end = stack.pop()
            if (begin >= 0 and end >= 0 and begin < end):
                pivotIdx = self._partition(begin, end, tuples)
                if (pivotIdx < k - 1):
                    stack.append((pivotIdx + 1, end))
                elif (pivotIdx > k - 1):
                    stack.append((begin, pivotIdx))
        return tuples

    def _partition(self, begin: int, end: int, tuples: List[Tuple[int, int]]) -> int:
        pivot = tuples[random.randint(begin, end - 1)]
        i = begin
        j = end
        while True:
            while tuples[i][1] > pivot[1]:
                i += 1

            while tuples[j][1] < pivot[1]:
                j -= 1

            if (i >= j):
                return j

            aux = tuples[i]
            tuples[i] = tuples[j]
            tuples[j] = aux
            i += 1
            j -= 1

    def _build_result_array(self, numsFrequency: List[Tuple[int, int]], k: int) -> List[int]:
        result = []
        for i in range(0, k):
            result.append(numsFrequency[i][0])
        return result

