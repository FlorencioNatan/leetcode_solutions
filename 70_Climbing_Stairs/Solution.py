
class Solution:
    def __init__(self) -> None:
        self.memoized = {}

    def climbStairs(self, n: int) -> int:
        if (n in self.memoized):
            return self.memoized[n]

        if (n == 1):
            return 1

        if (n == 2):
            return 2

        self.memoized[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return self.memoized[n]