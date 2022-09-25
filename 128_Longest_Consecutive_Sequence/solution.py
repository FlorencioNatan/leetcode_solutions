from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecSeq = dict()
        longestIntervalSize = 0
        for num in nums:
            if (num in consecSeq):
                continue

            nextNum = num + 1
            prevNum = num - 1
            startSeq = num
            endSeq = num

            if prevNum in consecSeq:
                startSeq = consecSeq[prevNum][0]

            if nextNum in consecSeq:
                endSeq = consecSeq[nextNum][1]

            numInterval = (startSeq, endSeq)
            consecSeq[startSeq] = numInterval
            consecSeq[endSeq] = numInterval

            if (longestIntervalSize < numInterval[1] - numInterval[0] + 1):
                longestIntervalSize = numInterval[1] - numInterval[0] + 1

            consecSeq[num] = numInterval

        return longestIntervalSize
