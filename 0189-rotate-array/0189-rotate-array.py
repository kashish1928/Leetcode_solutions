class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums)<2):
            return nums
        temp = []
        for i in nums:
            temp.append(i)
        k = k % len(nums)
        for i in range(0,len(nums)):
            nums[i] = temp[i-k]
            
        

        