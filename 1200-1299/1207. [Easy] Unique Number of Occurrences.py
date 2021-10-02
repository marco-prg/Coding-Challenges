# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = collections.Counter(collections.Counter(arr).values()).values()
        return sum(a) / len(a) == 1