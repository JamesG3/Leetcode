class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}                    # use a dictionary to save number and it's index in list freq
        i = 0
        freq = []                   # build a list to save number and it's frequency
        
        for n in nums:              # save numbers and their frequency into list freq
            if n not in dic:
                dic[n] = i
                i+=1
                freq.append([1,n])
            else:
                freq[dic[n]][0] += 1
                
        freq.sort(reverse = True)                   # sort cost O(nlogn) time
        
        res = []
        for count in xrange(k):
            res.append(freq[count][1])              # find a number in list freq cost O(1) time
            
        return res
                   
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        
        # Given a non-empty array of integers, return the k most frequent elements.
        # Given [1,1,1,2,2,3] and k = 2, return [1,2].
        # You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
        # Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
