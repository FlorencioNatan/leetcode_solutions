#!/usr/bin/env python3
from KthLargest import KthLargest
import random
from datetime import datetime

def main():
    # kth = KthLargest(5, random.sample(range(1_000_000), 500_000))
    # print(datetime.now().time())
    # for i in random.sample(range(1_000_0000), 500):
    #     kth.add(i)
    # print(datetime.now().time())
    # print(kth.isHeap())

    # kth = KthLargest(3, [4, 5, 8, 2])
    # print(kth.add(3))
    # print(kth.add(5))
    # print(kth.add(10))
    # print(kth.add(9))
    # print(kth.add(4))

    # kth = KthLargest(2, [0])
    # print(kth.add(-3))
    # print(kth.add(-2))
    # print(kth.add(-4))
    # print(kth.add(0))
    # print(kth.add(4))

    # [null,-1,1,1,2,3]
    kth = KthLargest(3, [5, -1])
    print(kth.add(2))
    print(kth.add(1))
    print(kth.add(-1))
    print(kth.add(3))
    print(kth.add(4))

if (__name__ == "__main__"):
    main()