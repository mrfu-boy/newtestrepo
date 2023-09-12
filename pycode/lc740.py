class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # 打家劫舍思路版
        all = [0 for i in range(max(nums)+1)]
        for num in nums:
            all[num] += 1

        ans = 0
        n = len(all)
        dp = [0] * n
        dp[0] = 0
        dp[1] = all[1]
        for i in range(2,n):
            dp[i] = max(i*all[i]+dp[i-2],dp[i-1])

        print(dp)
        return dp[n-1]



if __name__ == '__main__':
    nums = [2, 2, 3, 3, 3, 4]
    solution = Solution()
    solution.deleteAndEarn(nums)