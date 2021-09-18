# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        
        r_pointer = 0
        m_pointer = 0
        
        while r_pointer < len(ransomNote) and m_pointer < len(magazine):
            if ransomNote[r_pointer] == magazine[m_pointer]:
                r_pointer += 1
            m_pointer += 1
                
        return r_pointer == len(ransomNote)
    
    # O(m+n) with m and n being the lengths of the strings.
    # def canConstruct(self, ransomNote, magazine):
    #     return not collections.Counter(ransomNote) - collections.Counter(magazine)