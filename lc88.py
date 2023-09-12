class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos1 = m-1
        pos2 = n-1
        left = m + n - 1

        while pos1 > 0 and pos2 >= 0:
            if nums1[pos1] > nums2[pos2]:
                nums1[left] = nums1[pos1]
                pos1 -= 1
            else:
                nums1[left] = nums2[pos2]
                pos2 -= 1
            left -= 1

        print(nums1)



if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solu = Solution()
    solu.merge(nums1,m,nums2,n)