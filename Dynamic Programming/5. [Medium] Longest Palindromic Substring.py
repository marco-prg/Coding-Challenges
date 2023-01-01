# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        # Expand around center to find the longest palindromic substring
        def expand(left, right):        
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1            
            # Return (fixed) indexes of palindromic substring
            return left + 1, right - 1
        
        # We need to check starting from each character
        for i in range(len(s)):
            # We need to search for even and odd palindromes -> Starting values for right: equal to left and left+1
            for j in range(2):
                l, r = expand(i, i+j)

                # Update indexes if the len of the substring found > current len
                if r - l + 1 > end - start:
                    start = l
                    end = r
        
        return s[start : end+1]


# String - Dynamic Programming