# You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. 
# Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.
#
# Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.
#
# Implement the Solution class:
#  - Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
#  - int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        # Pick in the range [0, n-len(blacklist)-1]
        self.p = n - len(blacklist) - 1
        
        blacklist = set(blacklist)  # to avoid TLE
        
        # For the range [0, n-len(blacklist)-1], remapping of the blacklisted values ->
        # Mapping of all the whitelisted values in the first [0, n-len(blacklist)-1] values
        key = [x for x in blacklist if x < n - len(blacklist)]
        val = [x for x in range(n-len(blacklist), n) if x not in blacklist]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        # number in the range [0, n-len(blacklist)-1]        
        number = randint(0, self.p)
        # Return number if not in mapping, else the mapped value
        return self.mapping.get(number, number)


# Hash Table - Math - Binary Search - Sorting - Randomized