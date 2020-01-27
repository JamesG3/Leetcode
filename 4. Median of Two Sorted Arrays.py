class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        # 1 would be the shorter one
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
            
        s_l, s_r = 0, len1
        mid = int((len1 + len2 + 1) / 2)
        
        while s_l <= s_r:
            s_mid = int((s_l + s_r) / 2)
            l_mid = mid - s_mid
            
            # s_mid is too big
            if s_mid != 0 and nums1[s_mid-1] > nums2[l_mid]:
                s_r = s_mid - 1
            
            # s_mid is too small
            elif s_mid != len1 and nums1[s_mid] < nums2[l_mid-1]:
                s_l = s_mid + 1
            
            else:
                break
                
        # after we have the right position
        # to solve edge case: when len1 == len2
        if s_mid == 0:
            max_left = nums2[l_mid - 1]
        elif l_mid == 0:
            max_left = nums1[s_mid - 1]
        else:
            max_left = max(nums2[l_mid - 1], nums1[s_mid - 1])
        
        # if odd length
        if (len1 + len2) % 2:
            return max_left
        
        # if even length
        # to solve edge case: when len1 == len2
        if s_mid == len1:
            min_right = nums2[l_mid]
        elif l_mid == len2:
            min_right = nums1[s_mid]
        else:
            min_right = min(nums1[s_mid], nums2[l_mid])

        return (min_right + max_left) / 2
            
            
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Solution: Binary Search
        - find i, j to make len(A[:i]) + len(B[:j]) == len(A[i:]) + len(B[j:])
        - then compare the four numbers around these two locations
        - if odd, pick the left max
        - if even, pick the avg of the min_right and max_left
        
Time: O(log(min(m, n)))
Space: Extra O(1)
'''

