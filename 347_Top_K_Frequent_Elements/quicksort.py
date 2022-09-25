import random
from typing import List

class Quicksort:
    def runQuicksort(self, nums: List[int]) -> List[int]:
        self._quicksort(0, len(nums) - 1, nums)
        return nums

    def _quicksort(self, begin: int, end: int, nums: List[int]):
        if (begin >= 0 and end >= 0 and begin < end):
            idx_pivot = self._partition(begin, end, nums)
            self._quicksort(begin, idx_pivot, nums)
            self._quicksort(idx_pivot + 1 , end, nums)

    def _partition(self, begin: int, end: int, nums: List[int]) -> int:
        pivot = nums[random.randint(begin, end - 1)]
        i = begin
        j = end
        while True:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1

            if (i >= j):
                return j

            aux = nums[i]
            nums[i] = nums[j]
            nums[j] = aux
            i += 1
            j -= 1


if (__name__ == '__main__'):
    quick = Quicksort()
    # print([1,3,6,2,5,4,6])
    # print(quick.runQuicksort([1,3,6,2,5,4,6]))
    print([1,5,2,3,9,4,7,8,6])
    print(quick.runQuicksort([1,5,2,3,9,4,7,8,6]))

