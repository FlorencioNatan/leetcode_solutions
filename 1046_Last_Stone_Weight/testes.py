#!/usr/bin/env python3

from Solution import Solution

def main():
    sol = Solution()
    print(sol.lastStoneWeight([2,7,4,1,8,1]))
    print(sol.lastStoneWeight([1]))
    print(sol.lastStoneWeight([12, 37, 13]))
    print(sol.lastStoneWeight([2, 2]))


if (__name__ == '__main__'):
    main()