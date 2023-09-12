class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        while num >= 10:
            num = list(str(num))
            tmp_sum = 0
            for x in num:
                tmp_sum += int(x)
            num = int(tmp_sum)
            print(num)

        return num

if __name__ == '__main__':
    solu = Solution()
    solu.addDigits(38)