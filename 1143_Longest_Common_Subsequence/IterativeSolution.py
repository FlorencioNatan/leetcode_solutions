class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_array = []
        for i in range(len(text1)):
            dp_array.append([])
            for j in range(len(text2)):
                dp_array[i].append(0)
                if (text1[i] == text2[j]):
                    dp_array[i][j] = 1
                    if (i > 0 and j > 0):
                        dp_array[i][j] += dp_array[i-1][j-1]
                else:
                    dp_array[i][j] = max(dp_array[i][j-1], dp_array[i-1][j])

        return dp_array[len(text1) - 1][len(text2) - 1]
