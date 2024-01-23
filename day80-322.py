class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[math.inf]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for c in coins:
                if c<=i:
                    dp[i]=min(dp[i],dp[i-c]+1)
        
        if dp[amount]==math.inf:
            return -1
        else:
            return dp[amount]
