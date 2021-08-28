# Reverse bits of a given 32 bits unsigned integer.
# Note:
# -  Note that in some languages such as Java, there is no unsigned integer type. 
#    In this case, both input and output will be given as a signed integer type. 
#    They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# -  In Java, the compiler represents the signed integers using 2's complement notation. 
#    Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

class Solution:
    def reverseBits(self, n: int) -> int:
        l = "{0:b}".format(n)
        result = 0
        
        l2 = len(l)
        l3 = 32 - l2
        
        for i in range(l3):
            l = '0' + l 
            
        l = l[::-1]
        
        for i in range(len(l)):
            if int(l[i]):
                result += 2**(31-i)
            
        return result
        
    
    # Bit manipulation solution
    
    # def reverseBits(self, n):
    # ans = 0
    # for i in range(32):
    #     ans = (ans << 1) + (n & 1)
    #     n >>= 1
    # return ans