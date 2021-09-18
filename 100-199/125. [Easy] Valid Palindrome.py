# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s_filter = filter(str.isalnum, s)
        string = "".join(s_filter).lower()
        return string == string[::-1]
    
    # def isPalindrome(self, s: str) -> bool:
    #     beg = 0
    #     end = len(s) - 1
    #   
    #     while beg <= end:
    #         while not s[beg].isalnum() and beg < end:
    #             beg += 1
    #         while not s[end].isalnum() and beg < end:
    #             end -= 1
    #         if s[beg] == s[end] or s[beg].upper() == s[end].upper():
    #             beg += 1
    #             end -= 1
    #         else:
    #             return False
    #   
    #     return True