#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Solution import Solution
from ListNode import ListNode


def main() -> None:
    sol = Solution()
    ln11 = ListNode(4)
    ln12 = ListNode(0, ln11)
    ln13 = ListNode(2, ln12)
    ln11.next = ln13
    ln14 = ListNode(3, ln13)
    print(sol.hasCycle(ln14))
    print(sol.hasCycle(None))
    print(sol.hasCycle(ListNode(5)))

if (__name__ == "__main__"):
    main()
