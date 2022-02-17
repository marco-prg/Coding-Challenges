# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        
        for c in s:
            d[c] = d.get(c, 0) + 1
        
        for c in t:
            d[c] = d.get(c, 0) - 1
        
        for v in d.values():
            if v != 0:
                return False
        
        return True


# Hash Table - String - Sorting