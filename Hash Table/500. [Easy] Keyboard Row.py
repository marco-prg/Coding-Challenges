# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
# -  the first row consists of the characters "qwertyuiop",
# -  the second row consists of the characters "asdfghjkl", and
# -  the third row consists of the characters "zxcvbnm".

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        
        for word in words:
            current = set(word.lower())
            
            # Python set intersection -> & operator
            # check if current element is equal to one of these computed elements
            if current in (current & first, current & second, current & third):
                result.append(word)
                
        return result


# Array - Hash Table - String