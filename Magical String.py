class Solution(object):
    def magicalString(self, n):
        
        String = '1221121'              #initial String with length = 7
        i = 5                           #current mult index
        count = 4                       #current number of "1"
        
        if n<=7:                        #if the inut is lower than 7, count 1 in the substring
            String = String[:n]
            return String.count("1")
        
        countdown = n-7                 #if larger than 7, expand the string until it reach the length
        
        while countdown > 0:
            mult = int(String[i])       #find the times that next element needs to be appended
            
            if String[-1] == "1":
                String += '2'*mult      #expand the String
            else:
                String += "1"*mult        #if the next append element is 1, add count
                count+=mult
                
            countdown-=mult
            i+=1
            
        if countdown == -1 and String[-1] == "1":
            count-=1
            
        return count
        """
        :type n: int
        :rtype: int
        """
        
        #A magical string S consists of only '1' and '2' and obeys the following rules:
        #The first few elements of string S is the following: S = "1221121221221121122……"
        #If we group the consecutive '1's and '2's in S, it will be: 1 22 11 2 1 22 1 22 11 2 11 22 ......
        #You can see that the occurrence sequence above is the S itself.
        #Given an integer N as input, return the number of '1's in the first N number in the magical string S.
