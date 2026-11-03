class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set('aeiou')

        count = sum(c in vowels for c in s[:k])
        max_count = count

        for right in range(k, len(s)):
            if s[right - k] in vowels:
                count -= 1
            
            if s[right] in vowels:
                count += 1
            
            max_count = max(max_count, count)
            if max_count == k:
                return k

        return max_count       
