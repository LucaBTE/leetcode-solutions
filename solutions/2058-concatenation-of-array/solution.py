class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums[:]

        for n in nums:
            ans.append(n)
        return ans
