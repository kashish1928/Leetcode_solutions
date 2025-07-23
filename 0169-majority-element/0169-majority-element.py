class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        c = 1
        for i in range(1,len(nums)):
            if(nums[i-1]==nums[i]):
                c+=1
            if(c> floor(len(nums)/2)):
                return nums[i]
        return nums[0]