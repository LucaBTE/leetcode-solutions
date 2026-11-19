class Solution:
    def search(self, nums: list[int], target: int) -> int:


        # normal binary search

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2


            if nums[mid] == target:
                return mid

            # we know that one of the halfs is ordered, we don't know which one

            # this checks if the left part is ordered
            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]: #check if target is in the left part
                    right = mid - 1

                else:
                    left = mid + 1

            # if the left part is not ordered, then the right part is!
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1


        return -1
        
