class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        if n < 2:
            return 1

        dp = [1 for _ in range(n)]
        for i in range(n):

            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        print(dp)
        maxlable = dp.count(max(dp,key=dp.count))
        print(maxlable)

        return 1


if __name__ == '__main__':
    solu = Solution()
    nums = [1,3,5,4,7]

    solu.findNumberOfLIS(nums)