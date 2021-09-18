# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        stringX = "{0:b}".format(x)
        stringY = "{0:b}".format(y)
        
        if len(stringX) > len(stringY):
            stringY = "0" * (len(stringX) - len(stringY)) + stringY
        
        if len(stringY) > len(stringX):
            stringX = "0" * (len(stringY) - len(stringX)) + stringX
            
        result = 0
        
        for i in range(len(stringX)):
            if stringX[i] != stringY[i]:
                result += 1
        
        return result