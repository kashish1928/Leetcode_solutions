class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        left = 0
        summ = 0
        for right in range(len(nums)):
            summ+=nums[right]

            while(summ >= target):
                windowLen = right - left + 1
                minLen = min(minLen,windowLen)
                summ-=nums[left]
                left+=1

        if(minLen != float('inf')):
            return minLen
        return 0