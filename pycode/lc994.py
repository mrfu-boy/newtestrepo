import queue


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])

        q = queue.Queue()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.put([i,j])

        flags = [[False for _ in range(n)] for _ in range(m)]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans = 0
        while not q.empty():
            tmp_set = []
            while not q.empty():
                cur_pos = q.get()

                for d in direction:
                    newy,newx = cur_pos[0] + d[0],cur_pos[1] + d[1]
                    if newy < m and newy >= 0 and newx < n and newx >=0:
                        if flags[newy][newx] is False:
                            if grid[newy][newx] == 1:
                                tmp_set.append([newy,newx])
                                flags[newy][newx] = True
                                grid[newy][newx] = 2

            for pos in tmp_set:
                q.put(pos)
            if q.empty():
                break
            ans += 1

            for row in grid:
                if 1 in row: return -1
        print(ans)
        return ans




if __name__ == '__main__':
    solu = Solution()
    grid = [[1,2]]
    solu.orangesRotting(grid)