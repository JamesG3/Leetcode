class Solution(object):
    def fizzBuzz(self, n):
        ans=[]
        for n in range(1,n+1):
            if n%(3*5) == 0:              #check 15 first
                ans.append("FizzBuzz")
            elif n%3 == 0:
                ans.append("Fizz")
            elif n%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(n))
        return ans
        
        """
        
        Write a program that outputs the string representation of numbers from 1 to n.
        But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
        For numbers which are multiples of both three and five output “FizzBuzz”.
        
        :type n: int
        :rtype: List[str]
        """
