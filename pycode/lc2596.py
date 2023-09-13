
class Solution:
    def checkValidGrid(self, grid) -> bool:
        if grid[0][0] != 0:
            return False

        n = len(grid)
        indices = [[] for _ in range(n*n)]

        for i in range(n):
            for j in range(n):
                indices[grid[i][j]] = [i,j]
        for i in range(1,n*n,1):
            dx = abs(indices[i][0] - indices[i-1][0])
            dy = abs(indices[i][1] - indices[i-1][1])

            if dx * dy != 2:
                return False
        return True

if __name__ == '__main__':
    solu = Solution()
    #grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
    grid = [[0,3,6],[5,8,1],[2,7,4]]
    print(solu.checkValidGrid(grid))