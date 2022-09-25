from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valuesUsedInLines = []
        valuesUsedInColumns = []
        valuesUsedInQuadrants = []
        for i in range(len(board)):
            valuesUsedInLines.append(set())
            valuesUsedInColumns.append(set())
            valuesUsedInQuadrants.append(set())

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == '.'):
                    continue

                if (board[i][j] in valuesUsedInLines[i]):
                    return False
                valuesUsedInLines[i].add(board[i][j])

                if (board[i][j] in valuesUsedInColumns[j]):
                    return False
                valuesUsedInColumns[j].add(board[i][j])

                quadrantId = j // 3 + (i // 3) * 3
                if (board[i][j] in valuesUsedInQuadrants[quadrantId]):
                    return False
                valuesUsedInQuadrants[quadrantId].add(board[i][j])

        return True
