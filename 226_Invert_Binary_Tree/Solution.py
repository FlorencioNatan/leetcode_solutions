from typing import Optional
from TreeNode import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None):
            return None

        fifo = []
        fifo.append(root)
        while (len(fifo) > 0):
            current_node = fifo.pop()
            right_node = current_node.right
            current_node.right = current_node.left
            current_node.left = right_node
            if (current_node.right != None):
                fifo.append(current_node.right)
            if (current_node.left != None):
                fifo.append(current_node.left)

        return root

