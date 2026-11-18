class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        left = 0 
        right = len(nums) - 1

        idx = 0

        while left <= right:

            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
            
            elif nums[mid] < target:
                left = mid + 1

        return left
