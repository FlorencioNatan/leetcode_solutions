#!/usr/bin/env python3
from Solution import Solution


def main():
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))
    print(sol.missingNumber([0, 1]))
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
    print(sol.missingNumber([0, 1, 2 ,3, 4, 6]))
    print(sol.missingNumber([1, 2 ,3, 4, 5 , 6]))
    print(sol.missingNumber([0]))
    print(sol.missingNumber([1]))

if (__name__ == "__main__"):
    main()
