# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        if not len(nums1) or not len(nums2):
            return result
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
            
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

    # def intersection(self, nums1, nums2):
    #     set1 = set(nums1)
    #     set2 = set(nums2)
    #     return list(set2 & set1)


# Array - Hash Table - Two Pointers - Binary Search - Sorting