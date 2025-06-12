class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if(complement in numMap):
                return [numMap[complement],i]
            else:
                numMap[nums[i]] = i
        return []