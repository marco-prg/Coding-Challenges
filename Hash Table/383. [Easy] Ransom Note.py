# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        
        for c in magazine:
            d[c] = d.get(c, 0) + 1
        
        for c in ransomNote:
            d[c] = d.get(c, 0) - 1
        
        for v in d.values():
            if v < 0:
                return False
        
        return True
    
    # O(m+n) with m and n being the lengths of the strings.
    # def canConstruct(self, ransomNote, magazine):
    #     return not collections.Counter(ransomNote) - collections.Counter(magazine)


# Hash Table - String - Counting