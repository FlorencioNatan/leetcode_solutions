#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Solution import Solution


def main() -> None:
    sol = Solution()
    print(sol.search([-1,0,3,5,9,12], 9))
    print(sol.search([-1,0,3,5,9,12], 2))
    print(sol.search([1], 1))
    print(sol.search([1], 2))

if (__name__ == "__main__"):
    main()
