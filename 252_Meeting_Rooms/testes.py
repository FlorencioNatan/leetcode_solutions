#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Solution import Solution
from Interval import Interval

def main():
    sol = Solution()
    inte = [Interval(0,30), Interval(5,10), Interval(15,20)]
    print(sol.can_attend_meetings(inte))
    inte = [Interval(5,8), Interval(9,15)]
    print(sol.can_attend_meetings(inte))
    inte = [Interval(0,8), Interval(8,15)]
    print(sol.can_attend_meetings(inte))

if (__name__ == "__main__"):
    main()
