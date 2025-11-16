class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i, num in enumerate(nums):
            if(num not in mapping):
                mapping[num] = i
            else:
                if(abs(i - mapping[num]) <= k):
                    return True
                else:
                    mapping[num] = i

        return False