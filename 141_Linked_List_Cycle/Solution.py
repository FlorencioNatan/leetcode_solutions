from typing import Optional
from ListNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current_node = head
        while (current_node != None):
            if (current_node not in visited):
                visited.add(current_node)
            else:
                return True
            current_node = current_node.next
        return False
