class Solution(object):
    def reverseVowels(self, s):
        Vow="aeiouAEIOU"                #list the possible vowels as a string
        ls=list(s)                      #convert s into list for convenience
        tem=[]                          #create a empty list for storage move out vowels
        n=0                             #index for ls
        while n!= len(ls):              #read through ls and find vowels out, save them into tem
            if ls[n] in Vow:
                tem.append(ls[n])
                ls[n]="aa"              #and replace them with double characters
            n+=1
        m=0
        while len(tem)!=0:              #replace vowels in increase order with decrease items in tem
            if ls[m]=="aa":
                ls[m]=tem[-1]
                del tem[-1]
            m+=1
        
        return "".join(ls)
            
                
            
        """
        :type s: str
        :rtype: str
        
        Write a function that takes a string as input and reverse only the vowels of a string.
        Eg. Given s = "hello", return "holle". Given s = "leetcode", return "leotcede".
        :rtype: str
        """
        
