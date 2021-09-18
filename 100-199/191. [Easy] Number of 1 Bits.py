class Solution:
    def hammingWeight(self, n: int) -> int:
        l = "{0:b}".format(n)
        
        result = 0
        
        l = str(l)
        
        for e in l:
            if int(e):
                result += 1
                
        return result
    
    
#     Using bit operation to cancel a 1 in each round (&: and bitwise operator)
#     Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. 
#     n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
#
#     def hammingWeight(self, n):
#         c = 0
#         while n:
#             n &= n - 1
#             c += 1
#         return c