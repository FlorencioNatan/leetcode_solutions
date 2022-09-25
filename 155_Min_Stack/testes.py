#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from MinStack import MinStack


def main() -> None:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # return -3
    minStack.pop()
    print(minStack.top())    # return 0
    print(minStack.getMin()) # return -2

def teste2():
    ms = MinStack()
    ms.push(5)
    ms.push(4)
    ms.push(2)
    ms.push(1)
    ms.push(3)
    print(ms.getMin())
    print(ms.stack)
    print(ms.arr)

if (__name__ == "__main__"):
    main()
