class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        #暴力
        # n = len(nums)
        # ans = 0
        #
        # for left in range(n):
        #     cur_sum = 0
        #
        #     for right in range(left , n):
        #         cur_sum += nums[right]
        #         if cur_sum == k:
        #             ans += 1
        # print(ans)
        # return ans
        n = len(nums)
        prenum = [0 for _ in range(n)]
        prenum[0] = nums[0]
        count = 0
        numsset = set()
        numsset.add(prenum[0])
        numsset.add(0)

        for i in range(1,n):
            prenum[i] = prenum[i-1] + nums[i]
            if prenum[i] - k in numsset:
                count += 1
            numsset.add(prenum[i])

        print(prenum)
        print(count)
        return count


if __name__ == '__main__':
    solu = Solution()
    nums = [1,-1,0]
    k = 0
    solu.subarraySum(nums,k)