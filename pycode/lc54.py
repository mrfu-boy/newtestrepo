class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            matrix = list(zip(*matrix))[::-1]
        return res


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = list(zip(*matrix))[::-1]
    #solu.spiralOrder(matrix)
    print(matrix)