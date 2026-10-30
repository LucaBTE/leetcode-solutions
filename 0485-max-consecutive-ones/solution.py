class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        max = 0
        cnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
                if cnt > max:
                    max = cnt
            else:
                cnt = 0
        return max
            
        
