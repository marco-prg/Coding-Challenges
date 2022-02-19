# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0" * (len(b) - len(a)) + a
        b = "0" * (len(a) - len(b)) + b
            
        carry = 0
        result = ""
        sum_dict = {0: "0", 1: "1", 2: "0", 3: "1"}
        
        for i in range(len(a) - 1, -1, -1):
            num_a, num_b = int(a[i]), int(b[i]) 
            
            num_sum = num_a + num_b + carry
            result = sum_dict[num_sum] + result
            carry = num_sum > 1
        
        return "1" * carry + result


# Math - String - Bit Manipulation - Simulation