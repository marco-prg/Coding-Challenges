# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows (3) like this:
#
#     P   A   H   N
#     A P L S I I G
#     Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR" (result)
# Write the code that will take a string and make this conversion given a number of rows.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = [""] * numRows
        current = 0
        increment = -1
        
        for c in s:
            if current == 0 or current == numRows-1:
                increment = -increment
            result[current] += c
            current += increment
            
        return "".join(result)