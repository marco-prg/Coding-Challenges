# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        
        result = 0
        
        for i in str(num):
            result += int(i)
            
        return self.addDigits(result)


# Math - Simulation - Number Theory