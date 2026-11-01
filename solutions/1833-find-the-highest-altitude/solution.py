class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        

        max = 0
        total = 0

        for n in gain:
            total += n
            if total > max:
                max = total

        return max
