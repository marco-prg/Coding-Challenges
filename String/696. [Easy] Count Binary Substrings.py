# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counting = int(s[0])
        
        zero = 0
        uno = 0
        result = 0
        
        for i in s:
            number = int(i)
            
            if number == counting:                
                if number:
                    uno += 1
                else:
                    zero += 1
                    
            else:                
                result += min(zero, uno)                
                
                if number:
                    uno = 1
                else:
                    zero = 1
                    
                counting = number
        
        result += min(zero, uno)        
        return result


# Two Pointers - String