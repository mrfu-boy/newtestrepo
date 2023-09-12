class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m , n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if obstacleGrid[i-1][j] == 1:
                        if obstacleGrid[i][j-1] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] += dp[i][j-1]
                    else:
                        if obstacleGrid[i][j-1] == 1:
                            dp[i][j] += dp[i-1][j]
                        else:
                            dp[i][j] = dp[i][j-1] + dp[i-1][j]
        print(dp)
        return dp[m-1][n-1]


if __name__ == '__main__':
    solu = Solution()
    obstacleGrid = [[0,0],[0,1]]
    solu.uniquePathsWithObstacles(obstacleGrid)
