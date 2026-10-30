class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, n in enumerate(nums):
            m = target - n

            if m in seen:
                return [seen[m], i]
            
            seen[n] = i
