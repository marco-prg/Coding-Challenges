# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        
        for n in range(left, right + 1):                
            valid = True            
            for c in str(n):
                if c == '0' or n % int(c) != 0:
                    valid = False
                    break
            
            if valid:
                result.append(n)
        
        return result