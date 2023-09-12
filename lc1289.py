class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)

        dp = [[10**4 for _ in range(n)] for i in range(n)]

        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(n):

            for j in range(n):
                for k in range(n):
                    if k != j:
                        dp[i][j] = min(dp[i][j],dp[i-1][k]+grid[i][j])

        print(dp)
        return  min(dp[n-1])


if __name__ == '__main__':
    solu = Solution()
    grid = [[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2]]
    solu.minFallingPathSum(grid)