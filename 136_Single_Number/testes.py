#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Solution import Solution

def main():
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))
    print(sol.singleNumber([4, 1, 2, 1, 2]))
    print(sol.singleNumber([7]))
    print(sol.singleNumber([7, 5, 3, 5, 7, 3, 2, 8, 8, 9, 2]))

if (__name__ == "__main__"):
    main()