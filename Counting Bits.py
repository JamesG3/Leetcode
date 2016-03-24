class Solution(object):
    def countBits(self, num):
        ans=[]
        for i in range(0,num+1):
            ans.append(bin(i).count('1'))
        return ans
        """
        :type num: int
        :rtype: List[int]
        """
        #Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array. 
