class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ns = ''
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            ns += word1[i]
            ns += word2[i]
        
        ns += word1[min_len:]
        ns += word2[min_len:]
        return ns
        
