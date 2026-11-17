class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        first = nums[0]
        last = nums[k - 1]
        idx = 0

        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for n in nums[k:]:
            curr_sum = (curr_sum - nums[idx]) + n
            max_sum = max(max_sum, curr_sum)
            idx += 1
        
        return max_sum/k
        
