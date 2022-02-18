# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:        
        start = end = 0
        
        # checking each letter as start
        for i in range(len(s)):
            for j in range(2):                  # check for even and odd palindromes
                l, r = self.expand(s, i, i+j)

                if r - l + 1 > end - start:     # update indexes if substring len > current len
                    start = l
                    end = r
        
        return s[start : end+1]
    
    # Expand around center
    def expand(self, s, left, right):        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return left + 1, right - 1              # return indexes of palindrome string


# String - Dynamic Programming