#!/usr/bin/env python3

from Solution import Solution

def main():
    sol = Solution()
    print("{:032b}".format(1))
    print("{:032b}".format(sol.reverseBits(1)))
    print("{:032b}".format(4))
    print("{:032b}".format(sol.reverseBits(4)))
    print("{:032b}".format(5))
    print("{:032b}".format(sol.reverseBits(5)))
    print("{:032b}".format(12))
    print("{:032b}".format(sol.reverseBits(12)))

if (__name__ == "__main__"):
    main()
