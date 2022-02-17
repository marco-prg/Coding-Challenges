# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for _ in range(rowIndex):
            result = [1] + [c+d for c,d in zip(result, result[1:])] + [1]
        return result


# Array - Dynamic programming