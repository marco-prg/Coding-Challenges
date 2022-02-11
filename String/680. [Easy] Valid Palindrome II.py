# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        r = s[::-1]
        
        if s == r:
            return True
        
        for i in range(len(s)//2 + len(s)%2):
            if s[i] != r[i]:
                s = s[:i] + s[i+1:]
                r = r[:i] + r[i+1:]
                break
                
        return s == s[::-1] or r == r[::-1]


# Two Pointers - String - Greedy