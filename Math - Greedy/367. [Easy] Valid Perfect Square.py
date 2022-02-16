# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        p = 32
        
        while (n // (1 << p) < (1 << p)):
            p -= 1
        
        l, r = 1 << p, 1 << (p + 1)
        
        while r >= l:
            m = (l + r) // 2
            if n // m > m:
                l = m + 1
            elif n // m < m:
                r = m - 1
            else:
                break
        
        return n / m == m


# Math - Binary Search