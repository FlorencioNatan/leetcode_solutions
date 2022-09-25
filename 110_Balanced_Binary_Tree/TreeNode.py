class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return_str = str(self.val)
        if (self.left != None):
            return_str = return_str + " < ( " + self.left.__repr__() + " )"

        if (self.right != None):
            return_str = return_str + " > ( " + self.right.__repr__() + " )"

        return return_str
