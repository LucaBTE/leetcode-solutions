class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        missings = []
        numbers = list(range(1, len(nums) + 1))
        num_set = set(nums)
        
        for n in numbers:
            if n not in num_set:
                missings.append(n)
        return missings
        
