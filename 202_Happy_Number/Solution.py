class Solution:
    def isHappy(self, n: int) -> bool:
        numbers_already_seen = set()
        while (n != 1):
            if (n in numbers_already_seen):
                return False

            numbers_already_seen.add(n)
            n = self._nextNumber(n)

        return True

    def _nextNumber(self, n: int) -> int:
        str_n = str(n)
        next_number = 0
        for digit in str_n:
            int_digit = int(digit)
            next_number = next_number + pow(int_digit, 2)

        return next_number

