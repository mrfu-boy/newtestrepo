class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre = 0
        maxans = nums[0]
        n = len(nums)
        for right in range(n):
            pre = max(pre + nums[right], nums[right])
            maxans = max(maxans, pre)
        # print(prenums)
        return maxans



if __name__ == '__main__':
    solu = Solution()
    nums = [-1]
    solu.maxSubArray(nums)