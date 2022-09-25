from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for ch in s:
            if (ch == '(' or ch == '[' or ch == '{'):
                stack.append(ch)
            elif (len(stack) > 0):
                stack_top = stack.pop()
                if (stack_top != self.getCorrespondentParenthesis(ch)):
                    return False
            else:
                return False
        return len(stack) == 0

    def getCorrespondentParenthesis(self, paren):
        if (paren == ')'):
            return '('

        if (paren == ']'):
            return '['

        if (paren == '}'):
            return '{'

