class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        result = [[],[]]

        set1 = set(nums1)
        set2 = set(nums2)

        for n in set1:
            if n not in set2:
                result[0].append(n)
        for n in set2:
            if n not in set1:
                result[1].append(n)
        
        return result
        
