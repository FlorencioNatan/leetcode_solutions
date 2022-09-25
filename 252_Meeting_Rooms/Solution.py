from typing import List

from Interval import Interval

class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda k: k.start)
        for i in range(1, len(intervals)):
            current = intervals[i]
            previous = intervals[i-1]
            if (previous.end > current.start):
                return False
        return True
