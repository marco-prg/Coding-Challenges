# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([chr(ord(c) + 32) if ord(c) >= 65 and ord(c) <= 90 else c for c in s])