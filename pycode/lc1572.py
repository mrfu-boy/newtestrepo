class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n-i-1]
        ans -= mat[n//2][n//2]

        print(ans)
        return ans


if __name__ == '__main__':
    solu = Solution()
    mat = [[1]]
    solu.diagonalSum(mat)