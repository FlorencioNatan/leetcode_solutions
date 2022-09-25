#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Solution import Solution

def testes():
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1,1,1,2,2,3,4,4,4,4,4], 2))
    print(sol.topKFrequent([1], 1))
    print(sol.topKFrequent([0,0,0,0,0,1,1,1,2,2,3,7,8,8,8,8,8,8,5,5,5,5], 2))
    print(sol.topKFrequent([1,2], 2))
    print(sol.topKFrequent([1,2,3,3, 4, 4], 2))
    print(sol.topKFrequent([5,3,1,1,1,3,5,73,1], 3))

if (__name__ == "__main__"):
    testes()
