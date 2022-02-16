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
                
                if not grid[i][j]:
                    continue                    
                elif i == 0 and j == 0:
                    result += 4
                elif i == 0 and grid[i][j-1]:
                    result += 2
                elif i == 0:
                    result += 4
                elif j == 0 and grid[i-1][j]:
                    result += 2
                elif j == 0:
                    result += 4
                elif grid[i-1][j] and grid[i][j-1]:
                    continue
                elif grid[i-1][j] or grid[i][j-1]:
                    result += 2
                else:
                    result += 4
        
        return result


# Array - Matrix - Depth-First Search - Breadth-First Search