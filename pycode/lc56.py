class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals,key=lambda x:x[0])

        prestart , preend = intervals[0]
        n = len(intervals)
        newInterval = True
        ans = []

        for i,num in enumerate(intervals):
            curstart , curend = num
            if curstart > preend:
                ans.append([prestart,preend])
                prestart,preend = num
            else:
                preend = max(preend,curend)
            if i == n - 1:
                ans.append([prestart, preend])


        print(intervals)
        print(ans)
        return ans




if __name__ == '__main__':
    solu = Solution()
    intervals = [[1,4],[2,3]]
    solu.merge(intervals)