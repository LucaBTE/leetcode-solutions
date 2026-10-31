class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        max_candies = max(candies)
        result = []

        for c in candies:
            if c + extraCandies < max_candies:
                result.append(False)
            else:
                result.append(True)
        return result
            
