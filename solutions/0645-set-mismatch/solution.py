class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        duplicated = 0
        missing = 0

        seen = set()

        for n in nums:
            if n in seen:
                duplicated = n
            seen.add(n)
        
        for n in range(1, len(nums) + 1):
            if n not in seen:
                missing = n
                break
        
        return [duplicated, missing]

