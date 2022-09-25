from typing import Optional
from ListNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        current_node = head
        next_node = current_node.next
        current_node.next = None
        while (next_node != None):
            auxiliar_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = auxiliar_node

        return current_node
