class HitCounter(object):

    def __init__(self):
        self.record = {}
        """
        Initialize your data structure here.
        """
        

    def hit(self, timestamp):
        if timestamp in self.record:
            self.record[timestamp] += 1
        else:
            self.record[timestamp] = 1
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        

    def getHits(self, timestamp):
        counter = 0
        for i in xrange(timestamp-299, timestamp+1):
            if i in self.record:
                counter += self.record[i]
        return counter
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)




# Design a hit counter which counts the number of hits received in the past 5 minutes.
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). 
# You may assume that the earliest timestamp starts at 1.
# It is possible that several hits arrive roughly at the same time.
