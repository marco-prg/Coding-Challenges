# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:         
        positive = True
        
        if x < 0:
            x = -x
            positive = False
        
        result = int(str(x)[::-1])
            
        if result > (2 ** 31 - 1):
            return 0
            
        if not positive:
            result = -result
        
        return result