class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        
        read = 0

        for char in s:
            if char not in t[read:]:
                return False

            if read == len(t):
                return False

            while read < len(t):
                if t[read] == char:
                    read += 1
                    break
                read += 1
                
            
        return True
        
