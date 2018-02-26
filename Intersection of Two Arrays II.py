class Solution(object):
    
    # two pointers solution
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        res = []
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        
        while i<m and j<n:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1
        return res
                
            
        #using del to check every number in the nums1, if there is a same one in the nums2, then append it to ans and delete both of them from nums1 and nums2
        #if not, only del it from nums1.
        #when one of list is empty, end the loop.
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        Given two arrays, write a function to compute their intersection.
        """
        
