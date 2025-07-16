class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        j=0
        k=0
        while(k<len(nums)):
            if(nums[k]!=val):
                nums[j]=nums[k]
                j+=1
            else:
                count+=1
            k+=1
        return len(nums)-count