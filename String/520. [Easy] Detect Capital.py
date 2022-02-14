# We define the usage of capitals in a word to be right when one of the following cases holds:
#  - All letters in this word are capitals, like "USA".
#  - All letters in this word are not capitals, like "leetcode".
#  - Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        first_capital = word[0].isupper()
        second_capital = word[1].isupper()
        
        if not first_capital and second_capital:
            return False
        
        for w in word[2:]:
            if w.isupper() != second_capital:
                return False
            
        return True


# String