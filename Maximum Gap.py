class Solution(object):
    def maximumGap(self, nums):
        ans=[]
        num=sorted(nums)
        if(len(num)<2):
            return 0
        else:
            for i in range(0,len(num)-1):
                ans.append(num[i+1]-num[i])
        return max(ans)
        """
        :type nums: List[int]
        :rtype: int
        """
        #Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
        #Try to solve it in linear time/space.
        #Return 0 if the array contains less than 2 elements.
