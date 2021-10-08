# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example:
#   A -> 1
#   B -> 2
#   C -> 3
#   ...
#   Z -> 26
#   AA -> 27
#   AB -> 28 
#   ...

class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:                            # conversion to base 26
            n -= 1                              # maps 26 -> "Z"
            result += chr(n % 26 + ord('A'))    # ord('A') = 65
            n //= 26
        return result[::-1]