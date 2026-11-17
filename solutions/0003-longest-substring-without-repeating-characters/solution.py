class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_length = 0

        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1

            seen[c] = right
            max_length = max(max_length, right - left + 1)

        return max_length
