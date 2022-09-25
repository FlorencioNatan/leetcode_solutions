from ListNode import ListNode
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            return list2
        if (list2 == None):
            return list1

        if (list1.val <= list2.val):
            resulting_list = list1
            list1 = list1.next
        else:
            resulting_list = list2
            list2 = list2.next
        current_node = resulting_list

        while(list1 != None or list2 != None):
            if (list1 == None):
                current_node.next = list2
                return resulting_list
            if (list2 == None):
                current_node.next = list1
                return resulting_list

            if (list1.val <= list2.val):
                current_node.next = list1
                list1 = list1.next
                current_node = current_node.next
            else:
                current_node.next = list2
                list2 = list2.next
                current_node = current_node.next

        return resulting_list
