# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
# Note: You are not allowed to use any built-in library method to directly solve this problem.

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        d = "0123456789abcdef"      # like a map
        ans = ""
        
        # 32-bit int, one hex number is represented by 4 bits, so 32 / 4 = 8
        # works also for negative numbers: -26 // 16 = -2, -26 % 16 = 6
        
        for i in range(8):
            n = num % 16            # n = num & 15
            c = d[n]
            ans = c + ans
            num //= 16              # num >>= 4
            
        return ans.lstrip('0')      # strip leading zeroes (left strip)


# Math - Bit Manipulation