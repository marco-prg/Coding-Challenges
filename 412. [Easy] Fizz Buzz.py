# Given an integer n, return a string array answer (1-indexed) where:
# -  answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# -  answer[i] == "Fizz" if i is divisible by 3.
# -  answer[i] == "Buzz" if i is divisible by 5.
# -  answer[i] == i if non of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
        
        result = []
        
        for i in range(1,n+1):
            fizz = i % 3 == 0
            buzz = i % 5 == 0
            
            if fizz and buzz:
                result.append("FizzBuzz")
            elif fizz:
                result.append("Fizz")
            elif buzz:
                result.append("Buzz")
            else:
                result.append(str(i))
        
        return result