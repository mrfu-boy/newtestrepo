class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m,n = len(grid),len(grid[0])
        tag = [[False for _ in range(n)] for _ in range(m)]

        def dfs(posy,posx):
            tag[posy][posx] = True
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for d in direction:
                newy, newx = posy + d[0], posx + d[1]
                if newy < m and newy >= 0 and newx < n and newx >=0:
                    if tag[newy][newx] is False and grid[newy][newx] == '1':
                        dfs(newy,newx)

        islandcount = 0

        for i in range(m):
            for j in range(n):
                if tag[i][j] == False and grid[i][j] == '1':
                    dfs(i,j)
                    islandcount += 1
        print(islandcount)
        return islandcount





if __name__ == '__main__':
    solu = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
    solu.numIslands(grid)