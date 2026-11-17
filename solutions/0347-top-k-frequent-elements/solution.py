class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        seen = {}

        for n in nums:
            seen[n] = seen.get(n, 0) + 1

        lst = sorted(seen, key = seen.get, reverse = True)
        
        return lst[:k]
