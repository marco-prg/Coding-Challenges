# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Time complexity: O(NlogN) - Space complexity: O(1)

# O(N) Time solution:

# import heapq
# class Solution:
#     def maximumProduct(self, nums):
#         a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
#         return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])


# Array - Math - Sorting