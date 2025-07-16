class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i = 0
        j = 0
        s = []
        while(j<len(nums)):
            if(nums[j] not in s):
                nums[i] = nums[j]
                i+=1
                s.append(nums[j])
            else:
                count+=1
            j+=1
        return len(nums)-count