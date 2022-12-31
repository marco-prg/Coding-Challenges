# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

from itertools import product

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(ind, i, j):
            # Search over
            if self.found:
                return 

            # Search completed successfully
            if ind == k:
                self.found = True  
                return

            # Off-board
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            # Current letter
            tmp = board[i][j]

            # Not matching
            if tmp != word[ind]:
                return
            
            # Temporary replacing selected letter to avoid considering it twice or more
            board[i][j] = "#"

            # Searching for next letter in all adjacent cells
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                dfs(ind + 1, i+x, j+y)
            
            # Restoring letter
            board[i][j] = tmp
        
        # Init vars
        self.found = False
        m, n, k = len(board), len(board[0]), len(word)
        
        # Cartesian product -> to consider every cell as the starting point
        for i, j in product(range(m), range(n)):
            # Search over
            if self.found:
                return True
            # Starting dfs
            dfs(0, i, j)
        
        return self.found

# Complexity:
# - Time complexity is potentially O(m*n*3^k), where k is length of word and m and n are sizes of our board: 
#   We start from all possible cells of board, and each time (except first) we can go in 3 directions (we can not go back). 
#   In practice however this number will be usually much smaller, because we have a lot of dead-ends.
# - Space complexity is O(k) - potential size of our recursion stack.


# Array - Backtracking - Matrix
             