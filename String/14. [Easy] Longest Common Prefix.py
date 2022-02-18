# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min([len(s) for s in strs])        
        i = 0 
        
        while i < minlen:
            f = strs[0][i]
            
            for s in strs:
                if s[i] != f:
                    return s[:i]            
            i += 1
        
        return strs[0][:minlen]


# String