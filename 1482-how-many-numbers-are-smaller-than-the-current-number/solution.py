class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        seen = {}
        sorted_lst = sorted(nums)

        for i, n in enumerate(sorted_lst):
            if n not in seen:
                seen[n] = i
        return [seen[n] for n in nums]


