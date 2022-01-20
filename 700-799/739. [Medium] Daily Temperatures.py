# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for i,v in enumerate(temperatures):
            # Approach 1: Monotonic Stack
            # Pop until the current day's temperature is not warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < v:
                prev_i = stack.pop()
                answer[prev_i] = i - prev_i
                
            stack.append(i)
        
        return answer