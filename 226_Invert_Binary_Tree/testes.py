from TreeNode import TreeNode
from Solution import Solution

def main():
    sol = Solution()
    nd1 = TreeNode(1)
    nd2 = TreeNode(2)
    nd3 = TreeNode(3, nd1, nd2)
    nd4 = TreeNode(4)
    nd5 = TreeNode(5)
    nd6 = TreeNode(6, nd4, nd5)
    nd7 = TreeNode(7, nd3, nd6)
    print(nd7)
    print(sol.invertTree(nd7))

if (__name__ == "__main__"):
    main()

