# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. 
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, 
# which could be shorter than k but still must contain at least one character. 
# Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-', '')

        return "-".join([s[i-k if i > k else 0:i] for i in range(len(s), 0, -k)][::-1])

        
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-', '')

        result = ''
        
        l = len(s)
        
        n = l % k
        
        result = s[:n]
        
        if len(result) == l:
            return result
        
        if n != 0:        
            result += '-'
        
        for i in range(n, l, k):
            result += s[i:i+k]
            result += '-'
        
        return result[:-1]


# String