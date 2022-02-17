# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        for k,v in enumerate(columnTitle):
            result += (ord(v) - 64) * 26 ** (len(columnTitle) - 1 - k)
            
        return result


# Math - String