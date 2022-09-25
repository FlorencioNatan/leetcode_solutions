#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from solution import Solution

def main():
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(sol.longestConsecutive([-1,9,-3,-6,7,-8,-6,2,9,2,3,-2,4,-1,0,6,1,-9,6,8,6,5,2]))


if (__name__ == "__main__"):
    main()
