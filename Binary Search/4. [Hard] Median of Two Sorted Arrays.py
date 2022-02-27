# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # kth smallest number in the two sorted arrays
        def get_kth(start1, end1, start2, end2, k):
            if start1 > end1:
                return nums2[k-start1]
            if start2 > end2:
                return nums1[k-start2]

            middle1 = (start1 + end1) // 2
            middle2 = (start2 + end2) // 2
            middle1_value = nums1[middle1]
            middle2_value = nums2[middle2]

            # if k is bigger than the sum of median indices
            if (middle1 + middle2) < k:
                # if nums1 median value is bigger than nums2's, nums2's first half will always be positioned before nums1's median,
                # so k would never be in num2's first half
                if middle1_value > middle2_value:
                    return get_kth(start1, end1, middle2+1, end2, k)
                else:
                    return get_kth(middle1+1, end1, start2, end2, k)
            # if the sum of the two median indices is >= k
            else:
                # if nums1 median value is bigger than nums2's, nums2's first half would be merged before nums1's first half,
                # so k always come before nums1's median, then nums1's second half would never include k
                if middle1_value > middle2_value:
                    return get_kth(start1, middle1-1, start2, end2, k)
                else:
                    return get_kth(start1, end1, start2, middle2-1, k)
                
        len1 = len(nums1)
        len2 = len(nums2)
        # when total length is odd, the median is the middle
        if (len1 + len2) % 2:
            return get_kth(0, len1-1, 0, len2-1, (len1+len2) // 2)
        else:
        # when total length is even, the median is the average of the middle 2
            middle1 = get_kth(0, len1-1, 0, len2-1, (len1+len2) // 2 - 1)
            middle2 = get_kth(0, len1-1, 0, len2-1, (len1+len2) // 2)
            return (middle1 + middle2) / 2


# Array - Binary Search - Divide and Conquer