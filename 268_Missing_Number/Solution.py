from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            result = result ^ x

        if (len(nums) == 1):
            result = result ^ 1

        x = len(nums) + 1
        while x&(x-1) != 0:
            result = result ^ x
            x += 1

        return result
