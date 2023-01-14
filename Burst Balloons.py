class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]  # add the dummy head and tail, both are left till end and DO NOT burst them.
        dp = [[0] * len(nums) for _ in nums]
        for i in range(len(nums) - 3, -1, -1):
            for j in range(i + 2, len(nums)):
                dp[i][j] = max([dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j] for k in range(i + 1, j)])
        return dp[0][len(nums) - 1]