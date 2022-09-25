#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import solution

def main():
    sol = solution.Solution()
    resposta = sol.maxProfit([7,1,5,3,6,4])
    print(resposta)

    resposta = sol.maxProfit([7,6,4,3,1])
    print(resposta)

    resposta = sol.maxProfit([7])
    print(resposta)

    resposta = sol.maxProfit([70,10,50, 1,30,60,40])
    print(resposta)



if (__name__ == "__main__"):
    main()
