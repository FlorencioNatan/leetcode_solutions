#!/usr/bin/env python3

from Solution import Solution

def main():
    sol = Solution()
    print(sol.climbStairs(1))
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(5))
    print(sol.climbStairs(11))
    print(sol.climbStairs(12))
    print(sol.climbStairs(19))
    print(sol.climbStairs(20))
    print(sol.climbStairs(45))

if (__name__ == "__main__"):
    main()