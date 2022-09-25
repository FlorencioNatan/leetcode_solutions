from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.largest_than_kth = []
        for i in range(int(len(nums)/2), -1, -1):
            self._max_heapify_bubble_down(nums, i)

        if (len(nums) == 0):
            return

        range_limit = min(self.k, len(nums))
        for _ in range(range_limit):
            self.largest_than_kth.append(self._remove_largest(nums))

    def add(self, val: int) -> int:
        if (len(self.largest_than_kth) < self.k):
            self._append_on_a_sorted_list(self.largest_than_kth, val)
            return self.largest_than_kth[-1]

        if (val < self.largest_than_kth[-1]):
            return self.largest_than_kth[-1]

        self._append_on_a_sorted_list(self.largest_than_kth, val)
        self.largest_than_kth.pop()
        return self.largest_than_kth[-1]

    def _append_on_a_sorted_list(self, nums, val: int) -> None:
        i = 0
        j = len(nums)
        middle = int((i + j) / 2)
        while i < j:
            if (val <= nums[middle]):
                i = middle + 1
            if (val > nums[middle]):
                j = middle
            middle = int((i + j) / 2)

        nums.insert(middle, val)

    def _max_heapify_bubble_down(self, nums: List[int], pos: int):
        left = 2 * pos + 1
        right = 2 * pos + 2
        largest = pos

        if (left < len(nums) and nums[left] > nums[largest]):
            largest = left

        if (right < len(nums) and nums[right] > nums[largest]):
            largest = right

        if (largest != pos):
            aux = nums[largest]
            nums[largest] = nums[pos]
            nums[pos] = aux
            self._max_heapify_bubble_down(nums, largest)

    def _max_heapify_bubble_up(self, nums: List[int], pos: int):
        father = int((pos - 1)/2)

        if (nums[pos] < nums[father]):
            return

        aux = nums[father]
        nums[father] = nums[pos]
        nums[pos] = aux
        if (father != pos):
            self._max_heapify_bubble_up(nums, father)

    def _remove_largest(self, nums: List[int]) -> int:
        largest = nums[0]
        n = len(nums) - 1
        nums[0] = nums[n]
        nums.pop()
        self._max_heapify_bubble_down(nums, 0)
        return largest