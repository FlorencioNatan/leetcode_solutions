from typing import List
import math

class Solution:

   def search(self, nums: List[int], target: int) -> int:
        leftBound = 0
        rightBound = len(nums)
        while leftBound < rightBound:
            middleIndex = math.floor((leftBound + rightBound) / 2)
            if (target > nums[middleIndex]):
                leftBound = middleIndex + 1

            if (target < nums[middleIndex]):
                rightBound = middleIndex

            if (target == nums[middleIndex]):
                return middleIndex

        return -1

