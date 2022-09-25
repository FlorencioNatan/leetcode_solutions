from typing import Optional
from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0

        max_depth = 1
        fifo = []
        fifo.append((root, 1))
        while (len(fifo) > 0):
            current_node, depth = fifo.pop()
            if (depth > max_depth):
                max_depth = depth
            if (current_node.right != None):
                fifo.append((current_node.right, depth + 1))
            if (current_node.left != None):
                fifo.append((current_node.left, depth + 1))

        return max_depth

