# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        
        while digits[pointer] == 9:
            digits[pointer] = 0
            pointer -= 1
            
        if pointer < 0:
            digits.insert(0, 1)
        else:
            digits[pointer] += 1
        
        return digits


# Array - Math