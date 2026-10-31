class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:

        output = []
        
        for i in range(1, n+1):
            
            if i > target[-1]:
                break
            
            output.append("Push")
            if i not in target:
                output.append("Pop")                  

        
        return output
    
[1,3,4,6,7,8]
["Push","Push","Pop","Push","Push","Push","Pop","Push","Push","Push"]
