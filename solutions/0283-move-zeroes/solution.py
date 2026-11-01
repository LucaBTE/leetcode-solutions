class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # nums = [0,1,0,3,12]

        write = 0

        for read in range(len(nums)):
            if nums[read] == 0:
                continue
            if nums[write] == 0:
                nums[read], nums[write] = nums[write], nums[read]
            write += 1

