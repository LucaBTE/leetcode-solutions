class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        window_sum = sum(nums[:k])
        best = window_sum

        for i in range(k, len(nums)):
            window_sum -= nums[i - k]
            window_sum += nums[i]

            best = max(window_sum, best)

        return (best / k)
