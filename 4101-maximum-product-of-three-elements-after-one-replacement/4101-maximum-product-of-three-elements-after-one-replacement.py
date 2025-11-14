class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num = [abs(x) for x in nums]
        num.sort(reverse = True)
        return num[0]*num[1]*10**5
