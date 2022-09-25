#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Solution import Solution
from ListNode import ListNode


def main() -> None:
    sol = Solution()
    print(sol.reverseList(None))
    ln1 = ListNode(5)
    #print(sol.reverseList(ln1))
    ln2 = ListNode(3, ln1)
    #print(sol.reverseList(ln2))
    ln3 = ListNode(4, ln2)
    #print(sol.reverseList(ln3))
    ln4 = ListNode(15, ln3)
    print(sol.reverseList(ln4))

if (__name__ == "__main__"):
    main()
