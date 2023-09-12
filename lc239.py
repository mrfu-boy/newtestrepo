import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if k >= n:
            return [max(nums)]

        ans = []
        lookup = set()
        #先遍历前k个
        for i in range(k):
            lookup.add(nums[i])
        ans.append(max(lookup))
        left,right = 0,k
        for i in range(k,n):
            lookup.remove(nums[left])
            lookup.add(nums[right])
            ans.append(max(lookup))
            left += 1
            right += 1
        #print(ans)
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    nu = set(nums)
    print(max(nu))
    k = 3
    solu.maxSlidingWindow(nums,k)



