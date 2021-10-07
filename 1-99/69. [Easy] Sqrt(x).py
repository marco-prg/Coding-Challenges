# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        
        while x / (1 << i) >= (1 << i):
            i += 1
            
        # binary search        
        l = 1 << (i - 1) if i > 0 else 0
        r = l << 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            
            if mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
                
        
        # Newton method
        # r = x
        # while r*r > x:
        #     r = (r + x/r) / 2
        # return r