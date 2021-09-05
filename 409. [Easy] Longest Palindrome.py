# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        spare = False
        
        for v in collections.Counter(s).values():
            rem = v % 2
            result += v - rem
            
            if not spare and rem:
                result += rem
                spare = True
            
        return result