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

    nd8 = TreeNode(1)
    nd9 = TreeNode(2)
    nd10 = TreeNode(3, nd8, nd9)
    nd11 = TreeNode(4)
    nd12 = TreeNode(5)
    nd13 = TreeNode(6, nd11, nd12)
    nd14 = TreeNode(7, nd10, nd13)
    nd15 = TreeNode(9, nd7, nd14)
    print(sol.isSameTree(nd7, nd14))

if (__name__ == "__main__"):
    main()

