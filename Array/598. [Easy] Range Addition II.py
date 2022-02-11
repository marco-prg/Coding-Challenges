# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] 
# should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return the number of maximum integers in the matrix after performing all the operations.

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        # The * operator unpacks arguments in a function invocation statement -> repacking in row e col value arrays
        row, col = zip(*ops)
        # Matrix values after increments don't matter, we want the minimum submatrix (row, col) -> row * col = number of maximum integers
        return min(row) * min(col)


# Array - Math