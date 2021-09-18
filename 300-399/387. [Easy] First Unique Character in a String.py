# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        
        for i,v in enumerate(s):
            if counter[v] == 1:
                return i
        
        return -1
        