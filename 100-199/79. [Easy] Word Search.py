# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Complexity: Time complexity is potentially O(m*n*3^k), where k is length of word and m and n are sizes of our board: 
# we start from all possible cells of board, and each time (except first) we can go in 3 directions (we can not go back). 
# In practice however this number will be usually much smaller, because we have a lot of dead-ends. Space complexity is O(k) - potential size of our recursion stack.

from itertools import product

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(ind, i, j):
            if self.Found: return 

            if ind == k:
                self.Found = True  
                return 

            if i < 0 or i >= m or j < 0 or j >= n: return 
            tmp = board[i][j]
            if tmp != word[ind]: return

            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                dfs(ind + 1, i+x, j+y)
            board[i][j] = tmp
        
        self.Found = False
        m, n, k = len(board), len(board[0]), len(word)
        
        for i, j in product(range(m), range(n)):
            if self.Found: return True 
            dfs(0, i, j)
        return self.Found
    

#     def exist(self, board: List[List[str]], word: str) -> bool:
#         coord = {}
#        
#         for numRow, row in enumerate(board):
#             for numCol, elem in enumerate(row):
#                 if elem in word:
#                     if coord.get(elem):
#                         coord.get(elem).add((numRow, numCol))
#                     else:                        
#                         coord[elem] = {(numRow, numCol)}
#                        
#         # (coord_couple, word_start_position, coord_path)        
#         current = [(c, 0, set()) for c in coord.get(word[0], [])]
#       
#         while current:
#             c = current.pop()
#           
#             if c[1] == len(word)-1:
#                 return True
#           
#             accepted = {(c[0][0]+1,c[0][1]), (c[0][0]-1, c[0][1]), (c[0][0],c[0][1]+1), (c[0][0],c[0][1]-1)}
#             next_step = coord.get(word[c[1]+1], set()).intersection(accepted) - c[2]
#             current.extend([(n, c[1]+1, c[2].union({c[0]})) for n in next_step])
#       
#         return False
            
            
                
                