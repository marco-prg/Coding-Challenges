# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return result
        
        while len(matrix) > 0:
            row = matrix[0]
            last = len(row)
            
            for i in range(last):
                result.append(row[i])
            matrix.pop(0)
            
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return result
            
            for j in range(len(matrix)):
                result.append(matrix[j].pop(last-1))
                    
            row = matrix.pop(len(matrix)-1)
            row.reverse()
            
            for elem in row:
                result.append(elem)
                
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return result
            
            for k in range(-len(matrix)+1, 1):
                result.append(matrix[-k].pop(0))
        
        return result
    
#   def spiralOrder(self, matrix):
#       return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])