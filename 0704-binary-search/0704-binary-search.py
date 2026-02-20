class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
        
        l = 0
        u = len(nums)-1
        m = len(nums)//2

        while(l<=u):
            if(target == nums[m]):
                return m
            elif(target < nums[m]):
                u = m-1
                m = (u+l)//2
            else:
                l = m+1
                m = (u+l)//2
        return -1