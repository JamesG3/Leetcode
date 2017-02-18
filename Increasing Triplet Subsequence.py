class Solution(object):
    def increasingTriplet(self,nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:          #find the smallest element in every decreasing part
                first = n
            elif n <= second:       #after finding the first element, then find a number larger than the first one.
                second = n
            else:           #once met a number larger than second, then return True, or start over with the new value of first
                return True
        return False
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
        #Formally the function should:
        #Return true if there exists i, j, k 
        #such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
