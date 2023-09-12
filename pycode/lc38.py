class Solution:
    def countAndSay(self, n: int) -> str:

        def describeanumber(number):
            number = str(number)
            numbersize = len(number)
            if numbersize == 1:
                return '1' + str(number)
            prestr = number[0]
            ans = ''
            tmp_count = 0
            for i in range(numbersize):
                if prestr == number[i]:
                    tmp_count += 1
                else:
                    ans = ans + str(tmp_count) + str(prestr)
                    prestr = number[i]
                    tmp_count = 1
            ans = ans + str(tmp_count) + str(prestr)
            return ans

        number = 1
        for i in range(n):
            number = describeanumber(number)

        return number





if __name__ == '__main__':
    solu = Solution()

    solu.countAndSay(10)