# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

from math import prod

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        return prod(digits) - sum(digits)