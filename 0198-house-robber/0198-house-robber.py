class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums)
        
        dp = [0 for i in range(len(nums))]
        max_n = nums[0]
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            dp[i]=max_n + nums[i]
            max_n=max(max_n,dp[i-1])
        return max(dp)