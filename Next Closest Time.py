class Solution(object):

# simulation solution
    def nextClosestTime(self, time):
        numset = set([int(n) for n in time if n != ":"])
        time1 = 60 * int(time[:2]) + int(time[3:])
        diff1 = float('Inf')
        res1 = []
        diff2 = float('-Inf')
        res2 = []
        
        for i in xrange(24):
            hour = "0" + str(i) if i<10 else str(i)
            if not all(int(m) in numset for m in hour):
                continue
            for j in xrange(60):
                minute = "0" + str(j) if j<10 else str(j)
                if not all(int(m) in numset for m in minute):
                    continue
                time2 = i*60 + j - time1
                if 0 < time2 < diff1:
                    diff1 = time2
                    res1 = [hour, minute]
                elif time2 < 0 and -time2 > diff2:
                    diff2 = -time2
                    res2 = [hour, minute]
                    
        if res1 or res2:
            return ":".join(res1) if res1 else ":".join(res2)
        else:
            return time
                

        
        """
        :type time: str
        :rtype: str
        """
        
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
# There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
