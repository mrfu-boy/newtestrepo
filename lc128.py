class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)

        if n < 2:
            return n
        nums_set = set(nums)
        longest_streak = 0

        for num in nums:
            if (num - 1) not in nums_set:
                curr_streak = 1
                curr_num = num
                while curr_num + 1 in nums_set:
                    curr_streak += 1
                    curr_num += 1

                longest_streak = max(longest_streak,curr_streak)
        print(longest_streak)
        return longest_streak



if __name__ == '__main__':
    solu = Solution()
    nums = [100, 4, 200, 1, 3,6, 2,5]
    solu.longestConsecutive(nums)