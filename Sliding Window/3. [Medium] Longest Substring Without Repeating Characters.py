# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = start = 0
        seen = {}
        
        for i,v in enumerate(s):
            if v in seen and seen[v] >= start:                
                start = seen[v] + 1
            else:
                result = max(result, i - start + 1)
            seen[v] = i
        
        return result


# Hash Table - String - Sliding Window