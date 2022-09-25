#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from Solution import Solution
from IterativeSolution import Solution

def main():
    sol = Solution()
    print("abcde", "ace")
    print(sol.longestCommonSubsequence("abcde", "ace"))
    print("abc", "abc")
    print(sol.longestCommonSubsequence("abc", "abc"))
    print("abc", "def")
    print(sol.longestCommonSubsequence("abc", "def"))
    print("abcde", "akce")
    print(sol.longestCommonSubsequence("abcde", "akce"))
    print("abcde", "aace")
    print(sol.longestCommonSubsequence("abcde", "aace"))
    print("abcde", "aece")
    print(sol.longestCommonSubsequence("abcde", "aece"))


if (__name__ == "__main__"):
    main()
