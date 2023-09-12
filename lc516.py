class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for start in range(n-1,-1,-1):
            for end in range(n):
                if start >= end:
                    continue
                if s[start] == s[end]:
                    dp[start][end] = dp[start+1][end-1] + 2
                else:
                    dp[start][end] = max(dp[start+1][end],dp[start][end-1])
        print(dp)
        return dp[0][n-1]




if __name__ == '__main__':
    solu = Solution()
    s = "babbb"
    solu.longestPalindromeSubseq(s)