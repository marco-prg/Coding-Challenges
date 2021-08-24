# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result
        
        minlen = min([len(s) for s in strs])
        
        while minlen > 0:
            first = strs[0][:minlen]
            same = True
            
            for elem in strs:
                if elem[:minlen] != first:
                    same = False
                    break
            
            if same:
                return first
            
            minlen -= 1
        
        return result