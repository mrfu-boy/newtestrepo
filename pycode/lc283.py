class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        zero_pos = 0
        nozero_pos = 0

        while zero_pos <= nozero_pos and nozero_pos < n:
            while nums[zero_pos] != 0 and zero_pos < n-1:
                zero_pos += 1
            while nums[nozero_pos] == 0 and nozero_pos < n-1:
                nozero_pos += 1

            tmp = nums[zero_pos]
            nums[zero_pos] = nums[nozero_pos]
            nums[nozero_pos] = tmp
        print(nums)







if __name__ == '__main__':
    solu = Solution()
    nums = [0, 1, 0, 3, 12]
    solu.moveZeroes(nums)