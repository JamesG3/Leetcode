class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        Solution: using stack to store the indices, then calculate difference if condition is satisfied
        Time: O(n) - length of T
        Space: O(m) - number of distinct numbers
        """
        length = len(T)
        res = [0 for _ in xrange(length)]
        stack = []
        
        for i in xrange(length-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
                
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
            
        return res

# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
