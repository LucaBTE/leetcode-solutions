class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        result = {}

        for n in arr:
            result[n] = result.get(n, 0) + 1
            
        set1 = set(result.values())

        return len(result.values()) == len(set1)
        
