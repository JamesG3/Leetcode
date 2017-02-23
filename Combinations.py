class Solution(object):
    def combine(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:     #when x is larger than n or the number will be append to stack is larger than n, means the capcity of stack is not enough, so pop the current stack[-1] and append this value+1 to x.
                if not stack:                   #if all element in stack is poped, then there is no more combination
                    break
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
        return ans
                
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        
        #Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
        #For example,
        #If n = 4 and k = 2, a solution is:
        #[[2,4],  [3,4],  [2,3],  [1,2],  [1,3],  [1,4],]
