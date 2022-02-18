# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:         
        positive = x >= 0
        x = abs(x)        
        result = int(str(x)[::-1])
            
        if result > 2 ** 31 - 1:
            return 0
        
        return result if positive else -result


# Math