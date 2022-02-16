# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        arr = []
        
        while num > 0:
            arr.append(num % 2)
            num = num // 2
        
        arr = [0 if x else 1 for x in arr]
        
        for i,v in enumerate(arr):
            result += v * (2 ** i)          
        
        return result
        
    # Using XOR operator
    # def findComplement(self, num: int) -> int:        
    #     mask = 1 << (len(bin(num)) - 2)
    #     return (mask - 1) ^ num


# Bit Manipulation