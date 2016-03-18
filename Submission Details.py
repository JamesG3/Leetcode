class Solution(object):
    def romanToInt(self, s):
        count=0
        Sum=self.value(s[0])
        while(count<len(s)-1):
            if(self.value(s[count])<self.value(s[count+1])):
                Sum+=self.value(s[count+1])-2*self.value(s[count])
            else:
                Sum+=self.value(s[count+1])
            count+=1
        return Sum
        """
        :type s: str
        :rtype: int
        """
    def value(self,x):
        if(x=='I'):
            return 1
        elif(x=='V'):
            return 5
        elif(x=='X'):
            return 10
        elif(x=='L'):
            return 50
        elif(x=='C'):
            return 100
        elif(x=='D'):
            return 500
        elif(x=='M'):
            return 1000
