# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = []
        current = ""
        
        for i in range(len(s)):
            if i == 0:
                current = s[i]
                continue
            if s[i] not in current:
                current += s[i]
                continue
            else:
                words.append(current)
                index = current.index(s[i]) + 1
                current = current[index:] + s[i]
        words.append(current)
        
        return max([len(w) for w in words])
