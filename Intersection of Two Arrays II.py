class Solution(object):
    def intersect(self, nums1, nums2):
        ans=[]
        while len(nums1) != 0 and len(nums2) != 0:
            if nums1[0] in nums2:
                ans.append(nums1[0])
                del nums2[nums2.index(nums1[0])]
            del nums1[0]
        return ans
                
            
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
