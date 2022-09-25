#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Solution import Solution

def main():
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))
    print(sol.groupAnagrams(["aba", "casa", "saca", "tomas", "tamos", "roma", "amor", "roam"]))

if (__name__ == "__main__"):
    main()
