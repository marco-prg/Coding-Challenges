# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it in the maximum amount of balanced strings.
# Return the maximum amount of split balanced strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r, result = 0, 0, 0
        for digit in s:
            l, r = l + (digit == 'L'), r + (digit == 'R')
            if l > 0 and l == r:
                result += 1
                l, r = 0, 0
        return result


# String - Greedy - Counting