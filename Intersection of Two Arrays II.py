class Solution(object):
    def intersect(self, nums1, nums2):
        ans=[]
        while len(nums1) != 0 and len(nums2) != 0:
            if nums1[0] in nums2:
                ans.append(nums1[0])
                del nums2[nums2.index(nums1[0])]
            del nums1[0]
        return ans
                
            
        #using del to check every number in the nums1, if there is a same one in the nums2, then append it to ans and delete both of them from nums1 and nums2
        #if not, only del it from nums1.
        #when one of list is empty, end the loop.
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        Given two arrays, write a function to compute their intersection.
        """
        
