class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2
        self.memoized_values = {}
        return self.countLongestCommonSubsequence(len(text1) - 1, len(text2) - 1)

    def countLongestCommonSubsequence(self, idx_text1: int, idx_text2: int) -> int:
        if ((idx_text1, idx_text2) in self.memoized_values):
            return self.memoized_values[(idx_text1, idx_text2)]

        if (idx_text1 == -1 or idx_text2 == -1):
            return 0

        if (self.text1[idx_text1] == self.text2[idx_text2]):
            return 1 + self.countLongestCommonSubsequence(idx_text1 - 1, idx_text2 - 1)

        longest_common_subsequence = max(
                self.countLongestCommonSubsequence(idx_text1 - 1, idx_text2),
                self.countLongestCommonSubsequence(idx_text1, idx_text2 - 1)
        )
        self.memoized_values[(idx_text1, idx_text2)] = longest_common_subsequence
        return longest_common_subsequence

