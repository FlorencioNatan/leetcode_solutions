from typing import List, Tuple
from collections import deque

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self._solutions = []
        #print(self._nQueenInductive([], 0, n))
        print(self._nQueenInteractive(n))
        return self._solutions

    def _nQueenInteractive(self, n: int) -> int:
        stack = deque()
        stack.append(([], 0))
        total = 0
        while len(stack) > 0:
            queenList, startPos = stack.pop()
            if (len(queenList) == n):
                self._solutions.append(self._transformQueenTupleToString(queenList, n))
                total += 1

            for k in range(startPos, n*n):
                i = int(k/n)
                j = k % n
                if (self._isQueenPositionValid((i,j), queenList)):
                    newQueensList = [*queenList]
                    newQueensList.append((i,j))
                    stack.append((newQueensList, k + n - j))

        return total


# Com um loop
#     def _nQueenInductive(self, queenList: List[Tuple[int, int]], startPos: int, n: int) -> int:
#         if (len(queenList) == n):
#             self._solutions.append(self._transformQueenTupleToString(queenList, n))
#             return 1
# 
#         total = 0
#         #[[Proxima otimizição trocar esses loops por um só]]
#         for k in range(startPos, n*n):
#             i = int(k/n)
#             j = k % n
#             if (self._isQueenPositionValid((i,j), queenList)):
#                 newQueensList = list(queenList)
#                 newQueensList.append((i,j))
#                 total += self._nQueenInductive(newQueensList, k + (n - j), n)
# 
#         return total

#Com dois loops
#     def _nQueenInductive(self, queenList: List[Tuple[int, int]], startPos: int, n: int) -> int:
#         if (len(queenList) == n):
#             self._solutions.append(self._transformQueenTupleToString(queenList, n))
#             return 1
# 
#         total = 0
#         #[[Proxima otimizição trocar esses loops por um só]]
#         for i in range(n):
#             for j in range(n):
#                 currPos = i * n + j
#                 if (currPos < startPos):
#                     continue
#                 if (self._isQueenPositionValid((i,j), queenList)):
#                     newQueensList = list(queenList)
#                     newQueensList.append((i,j))
#                     total += self._nQueenInductive(newQueensList, (i + 1) * n, n)
# 
#         return total

    def _isQueenPositionValid(self, queen: Tuple[int, int], queenList: List[Tuple[int, int]]) -> bool:
        for q in queenList:
            if (q[0] == queen[0] or q[1] == queen[1] or abs(q[0] - queen[0]) == abs(q[1] - queen[1])):
                return False
        return True

    def _transformQueenTupleToString(self, queenList: List[Tuple[int, int]], n: int) -> List[str]:
        result = [["." for _ in range(n)] for _ in range(n)]

        for queen in queenList:
            result[queen[0]][queen[1]] = 'Q'

        for i in range(len(result)):
            result[i] = "".join(result[i])

        return result
