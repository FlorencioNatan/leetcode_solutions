from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_seen = {}
        for number in nums:
            if (number in number_seen):
                return True
            number_seen[number] = True
        return False
