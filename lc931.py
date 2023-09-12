class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j+1])
                elif j == n-1:
                    matrix[i][j] += min(matrix[i-1][j-1],matrix[i-1][j])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])

        print(matrix)
        return min(matrix[n-1])

if __name__ == '__main__':
    solu = Solution()
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    solu.minFallingPathSum(matrix)