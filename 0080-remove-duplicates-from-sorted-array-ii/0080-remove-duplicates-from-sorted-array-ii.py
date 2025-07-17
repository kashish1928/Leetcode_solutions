class Solution(object):
    def removeDuplicates(self, nums):
        c = 1
        index = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                c += 1
                if c <= 2:
                    nums[index] = nums[i]
                    index += 1
            else:
                c = 1
                nums[index] = nums[i]
                index += 1

        return index