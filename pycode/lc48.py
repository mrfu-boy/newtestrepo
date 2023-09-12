
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n):
            for j in range(n-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][n-i-1]
                matrix[n - j - 1][n - i - 1] = tmp

        for i in range(n//2):
            tmp = matrix[i]
            matrix[i] = matrix[n-i-1]
            matrix[n-i-1] = tmp

        print(matrix)


if __name__ == '__main__':
    solu = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solu.rotate(matrix)