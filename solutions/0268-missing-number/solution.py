class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        lst = range(0, len(nums) + 1)

        for n in lst:
            if n not in nums:
                return n
        
