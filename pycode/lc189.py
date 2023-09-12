class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        for i in range(n//2):
            tmp = nums[i]
            nums[i] = nums[n-i-1]
            nums[n-i-1] = tmp

        for i in range(k//2):
            tmp = nums[i]
            nums[i] = nums[k - i - 1]
            nums[k - i - 1] = tmp

        for i in range(k,k+(n-k)//2):
            tmp = nums[i]
            nums[i] = nums[k - i - 1]
            nums[k - i - 1] = tmp
        print(nums)

if __name__ == '__main__':
    solu = Solution()
    nums = [-1,-100,3,99]
    k = 2
    solu.rotate(nums,k)