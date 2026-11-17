class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:


        seen = {}

        for i, n in enumerate(nums):

            m = target - n

            if m in seen:
                return(seen[m], i)
            
            seen[n] = i


