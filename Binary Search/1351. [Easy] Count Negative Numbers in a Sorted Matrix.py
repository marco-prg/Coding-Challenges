# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0

        for row in grid:
            left = 0
            right = len(row)    # Used len(row) instead of len(row)-1 to have the correct result at line 19

            while left < right:
                middle = (left + right) // 2

                if row[middle] >= 0:
                    left = middle + 1
                else:
                    right = middle
            
            result += len(row) - right
        
        return result


# Array - Binary Search - Matrix