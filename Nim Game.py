class Solution(object):
    def canWinNim(self, n):
        return n%4!=0
        
        
        #if(n%4==0):
        #    return False
        #else:
        #    return True
        """
        You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

        Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap. 
        :type n: int
        :rtype: bool
        """
        #if n is 1,2,3 5,6,7 9,10,11 13,14,15 17,18,19.......... i can be the winner
        #when n is 4,8,12...... my friend always have the chance to make the number equal to 1,2,3 5,6,7......
        
