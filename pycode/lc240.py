import bisect
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #二分搜索
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            print(idx,idy)
            if idx < len(row) and row[idx] == target:
                return True
        return False



if __name__ == '__main__':
    solu = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 10
    solu.searchMatrix(matrix,target)