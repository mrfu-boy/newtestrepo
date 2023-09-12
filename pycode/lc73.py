class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m , n = len(matrix),len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for j in range(n):
                matrix[row][j] = 0

        for col in cols:
            for j in range(m):
                matrix[j][col] = 0


if __name__ == '__main__':
    solu = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solu.setZeroes(matrix)