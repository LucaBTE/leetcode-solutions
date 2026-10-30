class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        new_list = []

        for i in range (0, n):
            new_list.append(nums[i])
            new_list.append(nums[n + i])
        return new_list
