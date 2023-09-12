class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0],cost[1])

        dp = [0] * (n+1)
        for i in range(2,n+1):
            dp[i] = min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        print(dp)
        return dp[n-1]


if __name__ == '__main__':
    solu = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solu.minCostClimbingStairs(cost)