class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_dict = dict()
        n = len(nums)
        for i,num in enumerate(nums):
            if target - num in hash_dict:
                return [i,hash_dict[target-num]]
            hash_dict[num] = i
        return []




if __name__ == '__main__':
    solu = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    solu.twoSum(nums,target)