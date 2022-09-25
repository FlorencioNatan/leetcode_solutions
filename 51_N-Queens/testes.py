#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Solution import Solution
from datetime import datetime

def main():
    sol = Solution()
    print(datetime.now().time())
    (sol.solveNQueens(1))
    (sol.solveNQueens(2))
    (sol.solveNQueens(3))
    (sol.solveNQueens(4))
    (sol.solveNQueens(5))
    (sol.solveNQueens(6))
    (sol.solveNQueens(7))
    (sol.solveNQueens(8))
    (sol.solveNQueens(9))
    print(datetime.now().time())

if (__name__ == "__main__"):
    main()

