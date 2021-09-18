# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
# You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1            
        num2 = "0" * (len(num1) - len(num2)) + num2
        
        carry = 0        
        for i in range(-1, -len(num1)-1, -1):
            carry += ord(num1[i]) + ord(num2[i]) - 2*ord("0")
            result += str(carry % 10)
            carry //= 10
        
        if carry:
            result += str(carry % 10)
        
        return result[::-1]