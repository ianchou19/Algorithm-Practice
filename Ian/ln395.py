class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        if not values:
            return False
        if len(values) <= 2:
            return True

        n = len(values)

        # state: dp[i] 現在還剩i個硬幣，現在先取硬幣的人最後取得的最大總硬幣價值
        dp = [-1] * (n + 1)

        # intialize
        dp[0] = 0
        dp[1] = values[n - 1]
        dp[2] = values[n - 2] + values[n - 1]
        dp[3] = values[n - 3] + values[n - 2]

        # function
        for i in range(4, n + 1):
            # 換後手時, 後手會取對他而言最大值的路, 所以需要在這邊用 min (以先手觀點而言)
            # values[n - i] vs values[n - i] + values[n - i + 1] 為先手先取一個硬幣 or 取兩個硬幣的路線差別
            dp[i] = max(min(dp[i - 2], dp[i - 3]) + values[n - i],
                        min(dp[i - 3], dp[i - 4]) + values[n - i] + values[n - i + 1])

        # answer
        return dp[n] > (sum(values) / 2)

        # if not values:
        #     return False
        # if len(values) <= 2:
        #     return True

        # n = len(values)

        # # state: dp[i] 現在還剩i個硬幣，現在先取硬幣的人最後取得的最大總硬幣價值
        # dp = [-1] * (n + 1)

        # # intialize
        # dp[0] = 0
        # dp[1] = values[n - 1]
        # dp[2] = values[n - 2] + values[n - 1]
        # dp[3] = values[n - 3] + values[n - 2]

        # # function
        # for i in range(4, n + 1):
        #     if values[n - i + 1] - dp[i - 2] > values[n - i + 1] + values[n - i + 2] - dp[i - 3]:  # 樹左邊的後手觀點, 後手會從此條件中選擇對自己較利的
        #         tmp1 = values[n - i] + dp[i - 2]  # 先手往左走時會獲得的值
        #     else:
        #         tmp1 = values[n - i] + dp[i - 3]

        #     if values[n - i + 2] - dp[i - 3] > values[n - i + 2] + values[n - i + 3] - dp[i - 4]:  # 樹右邊的後手觀點, 後手會從此條件中選擇對自己較利的
        #         tmp2 = values[n - i] + values[n - i + 1] + dp[i - 3]  # 先手往左走時會獲得的值
        #     else:
        #         tmp2 = values[n - i] + values[n - i + 1] + dp[i - 4]

        #     dp[i] = max(tmp1, tmp2)

        #     # dp[i] = max(min(dp[i - 2], dp[i - 3]) + values[n - i], min(dp[i - 3], dp[i - 4]) + values[n - i] + values[n - i + 1])

        # # answer
        # return dp[n] > (sum(values) / 2)
