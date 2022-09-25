class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = s.lower()
        i = 0
        j = len(ls) - 1

        while (i <= j):
            chi = ls[i]
            chj = ls[j]
            if (self.isNotAlphanumeric(chi)):
                i += 1
            elif (self.isNotAlphanumeric(chj)):
                j -= 1
            elif (chi != chj):
                return False
            else:
                i += 1
                j -= 1

        return True

    def isNotAlphanumeric(self, ch) -> bool:
        if (ch >= 'a' and ch <= 'z'):
            return False

        if (ch >= '0' and ch <= '9'):
            return False

        return True

