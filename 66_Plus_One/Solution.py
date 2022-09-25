from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) -1, -1, -1):
            digits[i] += carry
            carry = 0
            if digits[i] == 10:
                digits[i] = 0
                carry = 1

            if (digits[i] != 0):
                break
        if (carry == 1):
            digits.insert(0,carry)
        return digits
