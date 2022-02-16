# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sx = "{0:b}".format(x)
        sy = "{0:b}".format(y)
        
        if len(sx) > len(sy):
            sy = "0" * (len(sx) - len(sy)) + sy
        
        if len(sy) > len(sx):
            sx = "0" * (len(sy) - len(sx)) + sx
            
        result = 0
        
        for i in range(len(sx)):
            if sx[i] != sy[i]:
                result += 1
        
        return result


# Bit Manipulation