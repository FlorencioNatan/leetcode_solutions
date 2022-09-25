#!/usr/bin/env python3
from Solution import Solution


def main():
    sol = Solution()
    print(sol.minCostClimbingStairs([10,15,20])) # 15
    print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) # 6

if (__name__ == '__main__'):
    main()