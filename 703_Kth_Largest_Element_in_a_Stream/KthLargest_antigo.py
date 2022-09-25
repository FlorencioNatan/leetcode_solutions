from turtle import right
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.largest_than_kth = []
        for i in range(int(len(nums)/2), -1, -1):
            self._max_heapify_bubble_down(i)

    def add(self, val: int) -> int:
        if (self.largest_than_kth == []):
            for _ in range(self.k - 1):
                self.largest_than_kth.append(self._remove_largest())
            return self.nums[0]

        if (val <= self.nums[0]):
            self._append_on_heap_and_bubble_up(val)
            return self.nums[0]

        self._append_on_larger_than_kth(val)
        new_kth_larger = self.largest_than_kth.pop()
        self._append_on_heap_and_bubble_up(new_kth_larger)

        return self.nums[0]

    def _append_on_heap_and_bubble_up(self, val: int) -> None:
        self.nums.append(val)
        self._max_heapify_bubble_up(len(self.nums) - 1)

    def _append_on_larger_than_kth(self, val: int) -> None:
        i = 0
        j = len(self.largest_than_kth)
        middle = int((i + j) / 2)
        while i < j:
            if (val <= self.largest_than_kth[middle]):
                i = middle + 1
            if (val > self.largest_than_kth[middle]):
                j = middle
            middle = int((i + j) / 2)

        self.largest_than_kth.insert(middle, val)

    def _max_heapify_bubble_down(self, pos):
        left = 2 * pos + 1
        right = 2 * pos + 2
        largest = pos

        if (left < len(self.nums) and self.nums[left] > self.nums[largest]):
            largest = left

        if (right < len(self.nums) and self.nums[right] > self.nums[largest]):
            largest = right

        if (largest != pos):
            aux = self.nums[largest]
            self.nums[largest] = self.nums[pos]
            self.nums[pos] = aux
            self._max_heapify_bubble_down(largest)

    def _max_heapify_bubble_up(self, pos):
        father = int((pos - 1)/2)

        if (self.nums[pos] < self.nums[father]):
            return

        aux = self.nums[father]
        self.nums[father] = self.nums[pos]
        self.nums[pos] = aux
        if (father != pos):
            self._max_heapify_bubble_up(father)

    def _remove_largest(self) -> int:
        largest = self.nums[0]
        n = len(self.nums) - 1
        self.nums[0] = self.nums[n]
        self.nums.pop()
        self._max_heapify_bubble_down(0)
        return largest

    def isHeap(self) -> bool:
        n = len(self.nums)
        for i in range(n):
            left_child = 2*i+1
            right_child = 2*i+2
            if (left_child < n and self.nums[left_child] > self.nums[i]):
                return False

            if (right_child < n and self.nums[right_child] > self.nums[i]):
                return False

        return True