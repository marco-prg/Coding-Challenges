# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []   
        
        if len(s) < len(p):
            return result
        
        current = {}
        
        # Collecting all p's letters
        for c in p:
            current[c] = current.get(c, 0) + 1

        # Checking with first len(p) letters of s    
        for i in range(len(p)):
            current[s[i]] = current.get(s[i], 0) - 1
        
        # If all current values are 0 -> anagram -> append index 0
        if all(not i for i in current.values()):
            result.append(0)
        
        right = len(p)
        
        # Starting Sliding Window
        while right < len(s):
            # Removing first letter (by adding 1 to letter value)
            current[s[right - len(p)]] = current.get(s[right - len(p)], 0) + 1
            # Adding current letter (by decrementing current letter value)
            current[s[right]] = current.get(s[right], 0) - 1
            
            # Checking if all current values are 0 -> anagram -> append index
            if all(not i for i in current.values()):
                result.append(right - len(p) + 1)
            
            right += 1
        
        return result


# Sliding Window - Hash Table - String