from typing import Optional
from TreeNode import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root == None):
            return True

        is_balanced = True
        depth = {}
        fifo = [root]
        while (len(fifo) > 0):
            current_node = fifo.pop()
            if (current_node not in depth):
                depth[current_node] = (1)
                fifo.append(current_node)

                if (current_node.right != None):
                    fifo.append(current_node.right)
                if (current_node.left != None):
                    fifo.append(current_node.left)
            else:
                l_depth = r_depth = l_diameter = r_diameter = 0
                if (current_node.left != None):
                    l_depth = depth[current_node.left]
                if (current_node.right != None):
                    r_depth = depth[current_node.right]

                if (abs(l_depth - r_depth) > 1):
                    is_balanced = False

                depth[current_node] = (max(l_depth + 1, r_depth + 1))

        return is_balanced

