class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ans = []
        start_idx = 0
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                if start_idx == i - 1:
                    ans.append(str(nums[start_idx]))
                else:
                    ans.append(f"{nums[start_idx]}->{nums[i-1]}")
                start_idx = i
                
        return ans