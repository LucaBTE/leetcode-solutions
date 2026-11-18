class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        n = len(temperatures)

        answer = [0] * n
        
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                previous_day = stack.pop()

                answer[previous_day] = i - previous_day
            
            stack.append(i)
        
        return answer
        
