#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import solution

def main():
    sol = solution.Solution()
    resposta = sol.twoSum([2, 3, 7, 5, 31, 127, 6, 79, 8], 12)
    #resposta = sol.twoSum([3, 3], 6)
    print(resposta)

if (__name__ == "__main__"):
    main()
