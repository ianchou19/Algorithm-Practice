class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        if n == 0:
            return False
        elif n == 1 or n == 2:
            return True

        dp = [False for _ in range(n+1)]
        dp[0] = False
        dp[1] = True
        dp[2] = True

        for i in range(3, n+1):
            # 換對手下棋時，對手面對剩下 i-1 or i-2 兩種情況都能獲勝 (暗示自己會輸)
            if dp[i-1] and dp[i-2]:
                dp[i] = False
            else:  # 換對手下棋時，對手面對剩下 i-1 or i-2 兩種情況的其中一種會輸 (暗示自己會贏)
                dp[i] = True

        return dp[n]
