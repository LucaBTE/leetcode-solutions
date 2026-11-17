class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        product = 1

        for i in range(len(nums)):
            result[i] = product
            product = product * nums[i]

        product = 1

        # with reversed() the list is read from right to left
        for i in reversed(range(len(nums))):
            result[i] = result[i] * product
            product = product * nums[i]

        return result
