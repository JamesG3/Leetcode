class Solution(object):
    def letterCombinations(self, digits):
        dic={"1":"*", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "0":" "}
        numbers=list(digits)
        global ans
        ans=[]
        self.Combination(numbers, dic)
        return ans
        
        
    def Combination(self, numbers, dic):
        global ans
        while len(numbers) != 0:
            if len(ans)==0:
                ans=list(dic[numbers[0]])
                numbers=numbers[1:]             #delete the first element
            else:
                possible=len(dic[numbers[0]])
                grouplen=len(ans)               #orignal length
                ans*=possible                   #new comination possibilities, expand orignal list
                index=0
                counter=0
                n=0
                while n != len(ans):
                    
                    if counter!=grouplen:
                        ans[n]+=dic[numbers[0]][index]
                        counter+=1
                        n+=1
                    elif counter==grouplen:
                        counter=0           #reset counter
                        index+=1
                numbers=numbers[1:]
                        
                
        """
        :type digits: str
        :rtype: List[str]
        """
        
        
        #Given a digit string, return all possible letter combinations that the number could represent.
        #A mapping of digit to letters (just like on the telephone buttons) is given below.
        #Example:
        #Input:Digit string "23"
        #Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].          
        
