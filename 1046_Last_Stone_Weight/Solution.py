from turtle import right
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(int(len(stones)/2), -1, -1):
            self._max_heapify_bubble_down(stones, i)

        while (len(stones) > 1):
            largest = self._remove_largest(stones)
            second_largest = self._remove_largest(stones)
            diff = largest - second_largest
            if (diff > 0):
                self._add_stone(stones, diff)
        
        if (len(stones) == 1):
            return stones[0]
        else:
            return 0

    def _remove_largest(self, stones: List[int]) -> int:
        largest = stones[0]
        last_element = stones.pop()
        if (len(stones) >= 1):
            stones[0] = last_element
        self._max_heapify_bubble_down(stones, 0)
        return largest

    def _max_heapify_bubble_down(self, stones: List[int], pos: int) -> None:
        left = 2 * pos + 1
        right = 2 * pos + 2
        largest = pos

        if (left < len(stones) and stones[pos] < stones[left]):
            largest = left

        if (right < len(stones) and stones[largest] < stones[right]):
            largest = right

        if (largest != pos):
            aux = stones[largest]
            stones[largest] = stones[pos]
            stones[pos] = aux
            self._max_heapify_bubble_down(stones, largest)

    def _add_stone(self, stones: List[int], diff: int) -> None:
        stones.append(diff)
        self._max_heapify_bubble_up(stones, len(stones) - 1)

    def _max_heapify_bubble_up(self, stones: List[int], pos: int) -> None:
        father = int((pos - 1) / 2)

        if (stones[father] < stones[pos]):
            aux = stones[father]
            stones[father] = stones[pos]
            stones[pos] = aux
            self._max_heapify_bubble_up(stones, father)
