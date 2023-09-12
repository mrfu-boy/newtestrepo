class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        dp = [[False for i in range(n)] for j in range(n)]
        ans = ''
        max_len = 0

        for first in range(n-1,-1,-1):
            for second in range(n):
                if first > second:
                    continue
                if first == second:
                    dp[first][second] = True
                elif first + 1 == second and s[first] == s[second]:
                    dp[first][second] = True
                else:
                    dp[first][second] = dp[first+1][second-1] and (s[first]==s[second])
                if dp[first][second] == True:
                    if second-first+1 > max_len:
                        ans = s[first:second+1]
                        max_len = second-first+1

        print(ans)
        return ans


if __name__ == '__main__':
    solu = Solution()
    s = "babad"
    solu.longestPalindrome(s)