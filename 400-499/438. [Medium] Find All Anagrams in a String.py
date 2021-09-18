# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []   
        
        if len(s) < len(p):
            return result
        
        current = {}
        
        for c in p:
            current[c] = current.get(c, 0) + 1
            
        for i in range(len(p)):
            current[s[i]] = current.get(s[i], 0) - 1
        
        if all(not i for i in current.values()):
            result.append(0)
        
        right = len(p)
        
        while right < len(s):
            current[s[right - len(p)]] = current.get(s[right - len(p)], 0) + 1
            current[s[right]] = current.get(s[right], 0) - 1
            
            if all(not i for i in current.values()):
                result.append(right - len(p) + 1)
            
            right += 1
        
        return result