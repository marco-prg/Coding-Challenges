# You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle 
# and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. 
# A point on the perimeter of a rectangle is included in the space covered by the rectangle.
#
# Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.
#
# Note that an integer point is a point that has integer coordinates.
#
# Implement the Solution class:
#  - Solution(int[][] rects) Initializes the object with the given rectangles rects.
#  - int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.rects_info = [0]
        total_points = 0
        
        for rect in rects:
            b = rect[2] - rect[0]
            h = rect[3] - rect[1]
            
            total_points += (b+1) * (h+1)
            self.rects_info.append(total_points)
        

    def pick(self) -> List[int]:
        # Total points = self.rects_info[-1]
        n = randint(0, self.rects_info[-1] - 1)
        # print(f"Point number = {n}")
        
        rect_number = self.get_rect_number(n)
        # print(f"Rect number = {rect_number}")
        
        rect = self.rects[rect_number]
        diff = n - self.rects_info[rect_number]
        # print(f"Diff = {diff}")        
        
        b = rect[2] - rect[0] + 1        
        row_number = diff // b
        col_number = diff % b
        # print(f"Row number = {row_number}")
        # print(f"Column number = {col_number}")
        
        x = rect[0] + col_number
        y = rect[3] - row_number
        # print(f"Selected point coord = [{x},{y}]\n")
        return (x, y)
        
    
    # Binary search
    def get_rect_number(self, target):
        l = 0
        r = len(self.rects_info) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if self.rects_info[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return r


# Math - Binary Search - Reservoir Sampling - Prefix Sum - Ordered Set - Randomized