# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        
        while num % 4 == 0:
            num //= 4
            
        return num == 1