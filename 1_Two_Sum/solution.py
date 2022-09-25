from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_total = dict()
        indices = dict()
        idx = 0
        for number in nums:
            if (number in sub_total):
                return [indices[target - number], idx]
            else:
                sub_total[target - number] = True
            indices[number] = idx
            idx += 1
        return []
