class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        char_in_s = dict()
        for ch in s:
            if (ch not in char_in_s):
                char_in_s[ch] = 1
            else:
                char_in_s[ch] += 1
        for ch in t:
            if (ch not in char_in_s):
                return False
            char_in_s[ch] -= 1
            if (char_in_s[ch] < 0):
                return False
        return True

