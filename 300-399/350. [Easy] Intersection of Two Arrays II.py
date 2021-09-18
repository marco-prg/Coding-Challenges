# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        if not len(nums1) or not len(nums2):
            return result
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        nums1.sort()
        nums2.sort()
            
        pointer1 = 0
        pointer2 = 0
        
        while pointer2 < len(nums2) and pointer1 < len(nums1):
            if nums2[pointer2] > nums1[pointer1]:
                pointer1 += 1
            elif nums2[pointer2] < nums1[pointer1]:
                pointer2 += 1
            else:
                result.append(nums2[pointer2])
                pointer1 += 1
                pointer2 += 1
        
        return result