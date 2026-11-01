class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        cnt = 0
        left = 0
        right = len(nums) - 1

        ord_nums = sorted(nums)

        while left < right:
            total = ord_nums[left] + ord_nums[right]

            if total == k:
                cnt += 1
                left +=1
                right -= 1
                continue
            elif total < k:
                left += 1
            else:
                right -= 1
        
        return cnt
