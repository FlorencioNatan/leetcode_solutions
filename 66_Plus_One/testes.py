#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Solution import Solution


def main():
    sol = Solution()
    print(sol.plusOne([1,2,3]))
    print(sol.plusOne([4,3,2,1]))
    print(sol.plusOne([9]))
    print(sol.plusOne([9,8,7]))
    print(sol.plusOne([9,9,9,9]))
    print(sol.plusOne([9,7,9,9]))

if (__name__ == "__main__"):
    main()
