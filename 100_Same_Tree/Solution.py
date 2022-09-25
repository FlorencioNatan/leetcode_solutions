from collections import deque
from TreeNode import TreeNode
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append((p, q))
        while len(stack) > 0:
            current_p, current_q = stack.pop()
            if ((current_p == None and current_q == None)):
                continue

            if ((current_p == None and current_q != None) or
                (current_p != None and current_q == None)):
                return False

            if (current_p.val != current_q.val):
                return False

            stack.append((current_p.left, current_q.left))
            stack.append((current_p.right, current_q.right))

        return True
