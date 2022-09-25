from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        current_total_product = 1
        for i in range(len(nums)):
            result[i] = current_total_product
            current_total_product *= nums[i]

        current_total_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= current_total_product
            current_total_product *= nums[i]

        return result
