class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if(nums[i] not in mapping):
                mapping[nums[i]] = [i]
            else:
                mapping[nums[i]].append(i)

        vals = [i for i in list(mapping.values()) if len(i) > 1]

        for i in vals:
            first = 0
            second = 1
            while(second < len(i)):
                if(abs(i[first]-i[second]) <= k):
                    return True
                else:
                    second+=1
                    first+=1
        return False