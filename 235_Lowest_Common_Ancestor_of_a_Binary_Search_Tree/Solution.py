from collections import deque
from TreeNode import TreeNode
from typing import Optional

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = deque()
        stack.append(root)
        min = self._min(p, q)
        max = self._max(p, q)
        while (len(stack) > 0):
            current_node = stack.pop()
            if (min.val <= current_node.val and max.val >= current_node.val):
                return current_node

            if (current_node.left != None):
                stack.append(current_node.left)
            if (current_node.right != None):
                stack.append(current_node.right)
        return root
    
    def _min(self, a: 'TreeNode', b: 'TreeNode'):
        if (a.val < b.val):
            return a
        return b

    def _max(self, a: 'TreeNode', b: 'TreeNode'):
        if (a.val > b.val):
            return a
        return b
