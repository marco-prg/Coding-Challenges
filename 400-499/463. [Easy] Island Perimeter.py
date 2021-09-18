# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):
                
                if grid[i][j]:
                    
                    if i == 0 and j == 0:
                        result += 4
                        continue
                    
                    if i == 0 and grid[i][j-1]:
                        result += 2
                        continue
                    
                    if i == 0:
                        result += 4
                        continue
                    
                    if j == 0 and grid[i-1][j]:
                        result += 2
                        continue
                        
                    if j == 0:
                        result += 4
                        continue
                        
                    if grid[i-1][j] and grid[i][j-1]:
                        continue
                        
                    if grid[i-1][j] or grid[i][j-1]:
                        result += 2
                        continue
                    
                    result += 4
        
        return result