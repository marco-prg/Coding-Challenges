# Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        positive = num > 0
        if not positive:
            num = -num
        
        result = ""
        
        while num > 0:
            result = f"{str(num % 7)}{result}"
            num = num // 7
        
        return result if positive else f"-{result}"