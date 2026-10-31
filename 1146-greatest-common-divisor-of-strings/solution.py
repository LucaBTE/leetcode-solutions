class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        shortest = str1 if len(str1) <= len(str2) else str2

        for i in range(len(shortest), 0, -1):
            candidate = shortest[:i]

            div1 = len(str1) // len(candidate)
            div2 = len(str2) // len(candidate)

            if (candidate * div1 == str1 and candidate * div2 == str2):
                return candidate
                
        return ''


