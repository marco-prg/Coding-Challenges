# The median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
#  - For example, for arr = [2,3,4], the median is 3.
#  - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#
# Implement the MedianFinder class:
#  - MedianFinder() initializes the MedianFinder object.
#  - void addNum(int num) adds the integer num from the data stream to the data structure.
#  - double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

# class MedianFinder:
#     def __init__(self):
#         self.array = []
#
#     def addNum(self, num: int) -> None:
#         self.array.append(num)
#
#     def findMedian(self) -> float:
#         self.array.sort()
#         h = len(self.array) // 2
#         if len(self.array) % 2 == 1:
#             return self.array[h]
#         else:
#             return (self.array[h - 1] + self.array[h]) / 2

from heapq import heappop, heappush     # python heap library

class MedianFinder:
    def __init__(self):
        self.leftHalf = []          # contains smallest numbers
        self.rightHalf = []         # contains highest numbers

    def addNum(self, num: int) -> None:
        # push in the left part opposite value in order to keep
        # the highest of the smallest in first position (becomes the smallest)
        heappush(self.leftHalf, -num)
        
        # push in the right part the highest value (not the opposite) from the left part
        # at each insertion in order to keep them balanced
        heappush(self.rightHalf, -heappop(self.leftHalf))
        
        # put the smallest of the right part back to left part (opposite value) if unbalanced
        if len(self.rightHalf) > len(self.leftHalf):
            heappush(self.leftHalf, -heappop(self.rightHalf))

    def findMedian(self) -> float:
        if len(self.leftHalf) > len(self.rightHalf):
            return -self.leftHalf[0]
        return (-self.leftHalf[0] + self.rightHalf[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()