class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        L = []
        R = []

        n = len(nums)
        lmulti = 1
        rmulti = 1
        for i in range(n):
            lmulti *= nums[i]
            rmulti *= nums[n-i-1]
            L.append(lmulti)
            R.append(rmulti)
        R.reverse()

        ans = []
        ans.append(R[1])
        for i in range(1,n-1):
            ans.append(L[i-1]*R[i+1])
        ans.append(L[n-2])
        print(ans)
        print(L)
        print(R)


if __name__ == '__main__':
    solu = Solution()
    nums = [-1,1]
    solu.productExceptSelf(nums)