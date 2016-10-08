class Solution(object):
    def countAndSay(self, n):
        res=['1']                                   #define the first number, save it into a list of string.
        if n == 0 or n == 1:                        #if n==1 or 0, return the first number.
            return res[-1]
        while n!=1:                                 #the countdown checkpoint, to count the time of loop
            tem=''                                  #set tem as a empty string to save the new string generated each time
            count=1                                 #number counter
            last=res[-1]
            for m in range(0,len(last)):            #count the string from 0 to the last digit
                if m != len(last)-1:                #count the string from 0 to the last second digit
                    if last[m]==last[m+1]:
                        count+=1
                    else:                           #if the next digit is not same
                        tem+= "%s" % count          #save count to tem
                        tem+= "%s" % last[m]        #then save the digit to tem
                        count=1                     #set count back to 1, prepare for the next use
                else:
                    if last[m] == last[m-1]:
                        tem+= "%s" % count
                        tem+= "%s" % last[m]
                        count=1
                    else:                           #if the last digit is not same
                        count=1                     #set count to 1
                        tem+= "%s" % count          #output the result
                        tem+= "%s" % last[m]
            res.append(tem)                         #save tem as a lastest string into res list
            n-=1                                    #countdown
            
        return res[-1]                              #return the last one in the list as the result
            
        
        """
        :type n: int
        :rtype: str
        
        The count-and-say sequence is the sequence of integers beginning as follows:
        1, 11, 21, 1211, 111221, ...
        always count the former number and return the last number
        """
        
