class Solution(object):
    
    # DFS solution
    def letterCombinations(self, digits):
        dic = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        
        if digits == "":
            return []
        
        elif len(digits) == 1:
            return dic[digits]
        
        else:
            res = []
            for n in dic[digits[0]]:
                for m in self.letterCombinations(digits[1:]):
                    res.append(n+m)
                    
            return res
                    
              
                
        """
        :type digits: str
        :rtype: List[str]
        """
        
        
        #Given a digit string, return all possible letter combinations that the number could represent.
        #A mapping of digit to letters (just like on the telephone buttons) is given below.
        #Example:
        #Input:Digit string "23"
        #Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].          
        
