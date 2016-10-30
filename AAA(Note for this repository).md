# TIPS

##ABOUT LeetCode
###List of tricky exercises
- Happy Number: *42 is an important number after experiments*

## ABOUT PYTHON
- For **list l**, using `l[::-1]` can return the reverse sequence of **list l**. `[::-1]` can also used in string or list like`[[1,2,3],[2,43,4],[3,4,5]]`


## Attentions
### If and while:
- *If* is a one-time check, what is required in the *if(requirement)* can change to any value or state in the *if block*.
- For example:
`a=2  
 if(a<=3):  
   while(a<6):  
     a+=1  
 return a`  
For this part of code, the final return value would be **5**, not **3**.
After a one-time check (a=2\<=3), the code in the *if block* can be executed, whatever the value of *a* becomes.
