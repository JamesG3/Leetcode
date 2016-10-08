class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l=m+n-1                      #used for index of the result nums1
        m-=1                         #used for index of nums1
        n-=1                         #used for index of nums2
        
        while m>=0 and n>=0:         #insert number from the largest
            if nums1[m]>=nums2[n]:   #compare numbers from nums1 and nums2 separately
                nums1[l]=nums1[m]
                m-=1
                l-=1
            else:
                nums1[l]=nums2[n]
                n-=1
                l-=1
        while n>=0:                  #insert the rest numbers of nums2 to nums1 if there is any.
            nums1[l]=nums2[n]
            n-=1
            l-=1
            
            
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        
        Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
        You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
        The number of elements initialized in nums1 and nums2 are m and n respectively.
        """
        
