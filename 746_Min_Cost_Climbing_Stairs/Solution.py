from cmath import cos
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self._memoized = {}
        return min(self._minCostRecursive(0, cost), self._minCostRecursive(1, cost))

    def _minCostRecursive(self, pos: int, cost: List[int]) -> int:
        if (pos in self._memoized):
            return self._memoized[pos]

        cost_one_step = cost_two_step = 0
        if (pos >= len(cost)):
            return 0

        cost_one_step = cost[pos] + self._minCostRecursive(pos + 1, cost)

        cost_two_step = cost[pos] + self._minCostRecursive(pos + 2, cost)

        self._memoized[pos] = min(cost_one_step, cost_two_step)
        return self._memoized[pos]

