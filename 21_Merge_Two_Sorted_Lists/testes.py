#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Solution import Solution
from ListNode import ListNode


def main() -> None:
    sol = Solution()
    print(sol.mergeTwoLists(None, None))
    ln11 = ListNode(5)
    ln12 = ListNode(3, ln11)
    ln13 = ListNode(2, ln12)
    ln14 = ListNode(1, ln13)

    ln21 = ListNode(8)
    ln22 = ListNode(4, ln21)
    ln23 = ListNode(2, ln22)
    ln24 = ListNode(1, ln23)
    print(sol.mergeTwoLists(ln14, ln24))

if (__name__ == "__main__"):
    main()
