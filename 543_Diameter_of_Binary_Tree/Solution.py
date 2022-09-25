from typing import Optional
from TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0

        depth_and_diameter = {}
        fifo = [root]
        while (len(fifo) > 0):
            current_node = fifo.pop()
            if (current_node not in depth_and_diameter):
                depth_and_diameter[current_node] = (1, 1)
                fifo.append(current_node)

                if (current_node.right != None):
                    fifo.append(current_node.right)
                if (current_node.left != None):
                    fifo.append(current_node.left)
            else:
                l_depth = r_depth = l_diameter = r_diameter = 0
                if (current_node.left != None):
                    l_depth, l_diameter = depth_and_diameter[current_node.left]
                if (current_node.right != None):
                    r_depth, r_diameter = depth_and_diameter[current_node.right]

                depth_and_diameter[current_node] = (max(l_depth + 1, r_depth + 1), max(l_diameter, r_diameter, l_depth + r_depth + 1))

        return depth_and_diameter[root][1] - 1

