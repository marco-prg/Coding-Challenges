# Given a characters array letters that is sorted in non-decreasing order and a character target,
# return the smallest character in the array that is larger than target.
#
# Note that the letters wrap around.
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        
        while r > l:
            m = (l + r) // 2
            
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        
        # Alternatively: bisect — Array bisection algorithm
        # r = bisect.bisect(letters, target)
        
        return letters[r % len(letters)]


# Array - Binary Search