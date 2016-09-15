class Solution(object):
    def intersection(self, nums1, nums2):
        nums1=set(nums1)
        nums2=set(nums2)
        r=[]
        for n in nums1:
            if n in nums2:
                r.append(n)
            else:
                continue
        return r
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Given two arrays, write a function to compute their intersection.
        Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
        """
