class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(abs(nums[0]),abs(nums[1]))
        max2 = min(abs(nums[0]),abs(nums[1]))
        for j in nums[2:]:
            i = abs(j)
            if(i > max1):
                max2 = max1
                max1 = i
            elif(i > max2):
                max2 = i
        return max1*max2*10**5
