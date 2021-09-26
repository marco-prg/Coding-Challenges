# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. 
# If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = [s[i:i+k] for i in range(0, len(s), k)]
        
        return "".join(v if i % 2 else v[::-1] for i,v in enumerate(temp))