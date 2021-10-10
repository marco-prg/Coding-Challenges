# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] 
# should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return the number of maximum integers in the matrix after performing all the operations.

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        r, c = zip(*ops)
        return min(r) * min(c)