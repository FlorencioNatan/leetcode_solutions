#!/usr/bin/env python3

from typing import List
import random
from datetime import datetime

class Heap:
    def montarHeapBubbleUp(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            self._maxHeapifyBubbleUp(nums, i)
        return nums

    def _maxHeapifyBubbleUp(self, nums: List[int], pos: int):
        father = int((pos - 1) / 2)

        if (nums[pos] < nums[father]):
            return
        else:
            aux = nums[father]
            nums[father] = nums[pos]
            nums[pos] = aux
        if (father != pos):
            self._maxHeapifyBubbleUp(nums, father)

    def montarHeapBubbleDown(self, nums: List[int]) -> List[int]:
        n2 = int(len(nums)/2)
        for i in range(n2, -1, -1):
            self._maxHeapifyBubbleDown(nums, i)
        return nums

    def _maxHeapifyBubbleDown(self, nums: List[int], pos: int):
        left_child = 2*pos+1
        right_child = 2*pos+2
        largest = pos

        if (left_child < len(nums) and nums[left_child] > nums[largest]):
            largest = left_child

        if (right_child < len(nums) and nums[right_child] > nums[largest]):
            largest = right_child

        if (largest != pos):
            aux = nums[largest]
            nums[largest] = nums[pos]
            nums[pos] = aux
            self._maxHeapifyBubbleDown(nums, largest)

    def isHeap(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            left_child = 2*i+1
            right_child = 2*i+2
            if (left_child < n and nums[left_child] > nums[i]):
                return False

            if (right_child < n and nums[right_child] > nums[i]):
                return False

        return True

def main():
    he = Heap()
    print(he.isHeap([1,2,3,4,5]))
    print(he.isHeap([5,4,3,2,1]))
    print(he.isHeap([5,3,4,1,2]))
    print(he.isHeap([5,4,1,3,2,-4,-7]))
    print(he.montarHeapBubbleUp([2,7,17,3,19,25,100,36,1]))
    print(he.montarHeapBubbleDown([2,7,17,3,19,25,100,36,1]))

    arraAntes = random.sample(range(10_000_000), 5_000_000)
    print(datetime.now().time())
    arrayDepois = he.montarHeapBubbleUp(arraAntes)
    print(datetime.now().time())
    isheap = he.isHeap(arrayDepois)
    print(isheap)

    arraAntes = random.sample(range(10_000_000), 5_000_000)
    print(datetime.now().time())
    arrayDepois = he.montarHeapBubbleDown(arraAntes)
    print(datetime.now().time())
    isheap = he.isHeap(arrayDepois)
    print(isheap)


# i: 0# father: 0
# i: 1# father: 0
# i: 2# father: 0
# i: 3# father: 1
# i: 4# father: 1
# i: 5# father: 2
# i: 6# father: 2
# i: 7# father: 3
# i: 8# father: 3
# i: 9# father: 4
# i: 10# father: 4

if (__name__ == '__main__'):
    main()