# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1].
# For this problem, assume that your function returns 2^31 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return -dividend - 1
        
        negative = (dividend >= 0) != (divisor > 0)
        dividend, divisor, result = abs(dividend), abs(divisor), 0
        
        for x in range(32)[::-1]:
            if dividend - (divisor << x) >= 0:
                result += 1 << x
                dividend -= divisor << x
                
        return result if not negative else -result


# Cannot store strings
#
# class Solution:
#     def division(self, dividend, divisor):
#         result = 0        
#         while dividend >= divisor:
#             dividend -= divisor
#             result += 1        
#         return str(result), str(dividend)
    
#     def divide(self, dividend: int, divisor: int) -> int:
#         if dividend == -2147483648 and divisor == -1:
#             return -dividend - 1
        
#         negative = (dividend >= 0) != (divisor > 0)
#         dividend = abs(dividend)
#         divisor = abs(divisor)
        
#         result = "0"
#         current = ""
        
#         for d in str(dividend):
#             current += d
#             r, current = self.division(int(current), divisor)
#             result += r           
        
#         return int(result) if not negative else -int(result)