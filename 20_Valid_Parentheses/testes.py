#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import solution

def main():
    sol = solution.Solution()

    resposta = sol.isValid("(")
    print(resposta)
    print("Devia ser False")

    resposta = sol.isValid("]")
    print(resposta)
    print("Devia ser False")

    resposta = sol.isValid("()[]{}")
    print(resposta)
    print("Devia ser True")

    resposta = sol.isValid("(]")
    print(resposta)
    print("Devia ser False")

    resposta = sol.isValid("(())")
    print(resposta)
    print("Devia ser True")

    resposta = sol.isValid("()[{}]")
    print(resposta)
    print("Devia ser True")

    resposta = sol.isValid("({[]})")
    print(resposta)
    print("Devia ser True")

    resposta = sol.isValid("({[)})")
    print(resposta)
    print("Devia ser False")

if (__name__ == "__main__"):
    main()
