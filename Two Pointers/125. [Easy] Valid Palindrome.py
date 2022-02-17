# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    # def isPalindrome(self, s: str) -> bool:        
    #     s_filter = filter(str.isalnum, s)
    #     string = "".join(s_filter).lower()
    #     return string == string[::-1]
    
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        while start <= end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            if s[start] == s[end] or s[start].upper() == s[end].upper():
                start += 1
                end -= 1
            else:
                return False
        
        return True


# Two Pointers - String