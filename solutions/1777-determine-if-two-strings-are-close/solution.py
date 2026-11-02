class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        map1 = {}
        map2 = {}

        if len(word1) != len(word2):
            return False

        for c in word1:
            map1[c] = map1.get(c, 0) + 1

        for c in word2:
            map2[c] = map2.get(c, 0) + 1
        
        if map1.keys() != map2.keys():
            return False
        list1 = sorted(map1.values())
        list2 = sorted(map2.values())

        return list1 == list2
        

            
