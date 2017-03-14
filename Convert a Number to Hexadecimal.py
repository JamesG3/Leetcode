class Solution(object):
    def toHex(self, num):
        
        if num >= 0:
            bina = bin(num)
        else:
            bina = bin(4294967296+num)
        res = ""
        bina = bina[2:]
        
        return self.helper(bina, res)
        
        
    def helper(self, bina, res):
        while len(bina) >= 4:
            tem = bina[-4:]
            bina = bina[:-4]
            tem = int(tem, 2)
            if tem < 10:
                res = str(tem)+res
            elif tem == 10:
                res = 'a'+res
            elif tem == 11:
                res = 'b'+res
            elif tem == 12:
                res = 'c'+res
            elif tem == 13:
                res = 'd'+res
            elif tem == 14:
                res = 'e'+res
            elif tem == 15:
                res = 'f'+res
        if len(bina) != 0:
            tem  = bina
            tem = int(tem, 2)
            if tem < 10:
                res = str(tem)+res
            elif tem == 10:
                res = 'a'+res
            elif tem == 11:
                res = 'b'+res
            elif tem == 12:
                res = 'c'+res
            elif tem == 13:
                res = 'd'+res
            elif tem == 14:
                res = 'e'+res
            elif tem == 15:
                res = 'f'+res
        return res
            
            
         
         
        """
        :type num: int
        :rtype: str
        """
        
        
        
        #Given an integer, write an algorithm to convert it to hexadecimal. 
