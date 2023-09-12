class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        res,l = 0,0

        while l < len(seats) and seats[l] == 0:
            l += 1
        res = max(l,res)
        while l < len(seats):
            r = l + 1
            while r < len(seats) and seats[r] == 0:
                r += 1
            if r == len(seats):
                res = max(res,r-l-1)
            else:
                res = max(res,(r-l)//2)
            l = r
        print(res)
        return res


if __name__ == '__main__':
    solu = Solution()
    seats = [1,0,0,0,1,0,1]
    solu.maxDistToClosest(seats)