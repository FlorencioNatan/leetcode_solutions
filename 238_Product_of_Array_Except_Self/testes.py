from Solution import Solution

def main():
    sol = Solution()
    print([1,2,3,4])
    print(sol.productExceptSelf([1,2,3,4]))
    print([-1,1,0,-3,3])
    print(sol.productExceptSelf([-1,1,0,-3,3]))
    print([])
    print(sol.productExceptSelf([]))
    print([0,2,0,4])
    print(sol.productExceptSelf([0,2,0,4]))
    print([0,2])
    print(sol.productExceptSelf([0,2]))

if (__name__ == '__main__'):
    main()
