# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        if len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b
            
        carry = 0
        result = ""
        sum_dict = {0: "0", 1: "1", 2: "0", 3: "1"}
        
        for i in range(len(a) - 1, -1, -1):
            num_a = int(a[i])
            num_b = int(b[i])
            
            num_sum = num_a + num_b + carry
            result = sum_dict[num_sum] + result
            carry = 1 if num_sum > 1 else 0
        
        return "1" + result if carry else result