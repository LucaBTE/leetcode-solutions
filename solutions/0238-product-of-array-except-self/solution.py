class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        seen = {}
        result = []

        for i, n in enumerate(nums):

            if n in seen:
                result.append(seen[n])
                continue

            prod = 1

            for j, m in enumerate(nums):
                if i == j:
                    continue
                else:
                    prod *= m

            seen[n] = prod
            result.append(prod)
        return result
