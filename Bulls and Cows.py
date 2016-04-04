class Solution(object):
    def getHint(self, secret, guess):
        Acount=0
        Bcount=0
        count=0
        Se={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        Gu={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        while(count<len(secret)):
            if(secret[count]==guess[count]):
                Acount+=1
                count+=1

            else:
                Se[secret[count]]+=1
                Gu[guess[count]]+=1
                count+=1

        for n in Se:
            if(Se[n]>=Gu[n]):
                Bcount+=Gu[n]
            else:
                Bcount+=Se[n]

        return '%dA%dB'%(Acount,Bcount)
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #You are playing the following Bulls and Cows game with your friend: 
        #You write down a number and ask your friend to guess what the number is. 
        #Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") 
        #and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
