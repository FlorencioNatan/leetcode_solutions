class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val) + "->" + self.next.__repr__()

