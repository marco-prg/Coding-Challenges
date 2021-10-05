# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()

        for i,n in enumerate(nums):
            # make sure the rightmost one is the smallest
            while len(queue) and nums[queue[-1]] <= n:
                queue.pop()

            # append index
            queue.append(i)

            # make sure the leftmost one is in-bound
            if i - queue[0] >= k:
                queue.popleft()

            # if i + 1 < k, then we are initializing the queue array
            if i + 1 >= k:
                result.append(nums[queue[0]])
        return result


#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k == 1:
#             return nums
#             
#         queue = deque([nums[0]])
#         current = nums[0]
#        
#         for i in range(1, k):
#             while len(queue) and queue[-1] < nums[i]:
#                 queue.pop()
#             current = max(current, nums[i])
#             queue.append(nums[i])
#        
#         lost_max = current == nums[0]
#         result = [current]
#         queue.popleft()
#        
#         for i in range(1, len(nums)-k+1):
#             if nums[i+k-1] > current:
#                 current = nums[i+k-1]
#                 queue.clear()
#             else:
#                 while len(queue) and queue[-1] < nums[i+k-1]:
#                     queue.pop()                                 
#                 queue.append(nums[i+k-1])
#                 current = current if not lost_max else queue.popleft()             
#             result.append(current)
#             lost_max = current == nums[i]
#            
#         return result


    
        