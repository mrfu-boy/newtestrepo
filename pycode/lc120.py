class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)

        if n == 1:
            return triangle[0][0]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])

        print(triangle)
        return triangle[0][0]




if __name__ == '__main__':
    solu = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    solu.minimumTotal(triangle)