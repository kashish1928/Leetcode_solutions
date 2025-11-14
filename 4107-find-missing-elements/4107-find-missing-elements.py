class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        num = set(nums)
        for i in range(min(nums),max(nums)):
            if(i not in num):
                ans.append(i)
        return ans