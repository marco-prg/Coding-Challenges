# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

class Solution:
    def reverseVowels(self, s: str) -> str:
        result = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        left = 0
        right = len(result)-1
        
        while left < right:
            if result[left] not in vowels:
                left += 1
            elif result[right] not in vowels:
                right -= 1
            else:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1
        
        return "".join(result)