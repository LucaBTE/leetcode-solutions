class Solution:
    def reverseWords(self, s: str) -> str:
        
        lst = []
        
        lst = s.split(' ')

        lst[:] = [w for w in lst if w != '']

        lst = lst[::-1]

        return(' '.join(lst))
