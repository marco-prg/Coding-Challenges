# There is an m x n matrix that is initialized to all 0's. 
# There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
#
# For each location indices[i], do both of the following:
#  - Increment all the cells on row ri.
#  - Increment all the cells on column ci.
#
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0 for i in range(m)]
        matrix = [rows.copy() for i in range(n)]        
            
        for elem in indices:
            for i in range(m):
                matrix[elem[0]][i] += 1
            for i in range(n):
                matrix[i][elem[1]] += 1
            
        return sum([e % 2 for rows in matrix for e in rows])