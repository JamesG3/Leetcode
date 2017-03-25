class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        
        length = len(timeSeries)
        ans = 0
        
        if length == 0:
            return ans
        
        for i in xrange(1, length):
            ans += min(duration, timeSeries[i] - timeSeries[i-1])
        return ans+duration
        
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        
        #In LLP world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.
        #You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.
