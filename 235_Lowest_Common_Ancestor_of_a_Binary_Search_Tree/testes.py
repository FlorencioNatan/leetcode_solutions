from TreeNode import TreeNode
from Solution import Solution

def main():
    sol = Solution()
    nd1 = TreeNode(1)
    nd2 = TreeNode(3)
    nd3 = TreeNode(2, nd1, nd2)
    nd4 = TreeNode(5)
    nd5 = TreeNode(7)
    nd6 = TreeNode(6, nd4, nd5)
    nd7 = TreeNode(4, nd3, nd6)

    nd8 = TreeNode(9)
    nd9 = TreeNode(11)
    nd10 = TreeNode(10, nd8, nd9)
    nd11 = TreeNode(13)
    nd12 = TreeNode(15)
    nd13 = TreeNode(14, nd11, nd12)
    nd14 = TreeNode(12, nd10, nd13)
    nd15 = TreeNode(8, nd7, nd14)
    print(sol.lowestCommonAncestor(nd15, nd11, nd8))

if (__name__ == "__main__"):
    main()

