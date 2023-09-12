class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 1

        dp = [1 for i in range(n)]
        for i in range(n):
            max_dp = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        #print(dp)
        return max(dp)


if __name__ == '__main__':
    solu = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    solu.lengthOfLIS(nums)