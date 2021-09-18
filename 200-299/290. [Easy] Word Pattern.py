# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        word_dict = {}
        pattern_dict = {}
        
        if len(words) != len(pattern):
            return False
        
        for i,v in enumerate(words):
            curr_pattern = pattern[i]
            
            if not word_dict.get(v):
                word_dict[v] = curr_pattern
            else:
                if word_dict[v] != curr_pattern:
                    return False
            
            if not pattern_dict.get(curr_pattern):
                pattern_dict[curr_pattern] = v
            else:
                if pattern_dict[curr_pattern] != v:
                    return False
            
        return True