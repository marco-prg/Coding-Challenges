# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

from heapq import heappop, heappush

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []

        # Explanation: page 127 Skiena

        # Initializing with the first pair (0,0)
        # Storing a tuple with the sum of values as key for the heap, plus the indexes (i,j)
        # We need the indexes to put the next possible minimum pairs in the heap - (i+1, j) and (i, j+1)
        # when we pop a tuple from the heap
        heap = [(nums1[0] + nums2[0], 0, 0)]

        # we need to keep the history of seen pairs, because we can't consider them more than once
        visited = set((0,0))
        
        # k can be greater than the number of all possible combinations, so we need to check heap       
        while heap and k > len(result):
            _, i, j = heappop(heap)
            result.append((nums1[i], nums2[j]))
            
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
        
        return result


# Array - Heap (Priority Queue)