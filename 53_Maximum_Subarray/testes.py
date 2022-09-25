#!/usr/bin/env python3
from Solution import Solution

def main():
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
    print(sol.maxSubArray([1])) # 1
    print(sol.maxSubArray([5,4,-1,7,8])) # 23
    print(sol.maxSubArray([1, 2, 3, 4, 5])) # 23
    print(sol.maxSubArray([7, 8, 9, 10])) # 23
    print(sol.maxSubArray([1, 2, 3, 4, 5, -14, 7, 8, 9, 10])) # 23
    print(sol.maxSubArray([-2, -1])) # 1


if (__name__ == '__main__'):
    main()
