# TIPS

## ABOUT LeetCode
### List of tricky exercises
- Happy Number: *42 is an important number after experiments*

## ABOUT PYTHON
### Useful Tools
#### [::-1]
- For **list l**, using `l[::-1]` can return the reverse sequence of **list l**. `[::-1]` can also used in string or list like`[[1,2,3],[2,43,4],[3,4,5]]`
#### zip
- 


### Attentions
#### If and while:
- *If* is a one-time check, what is required in the *if(requirement)* can change to any value or state in the *if block*.
- For example:`a=2` `if(a<=3):` `while(a<6):` `a+=1`  
	 `return a`  
	For this part of code, the final return value would be **5**, not **3**.
	After a one-time check (a=2\<=3), the code in the *if block* can be executed, whatever the value of *a* becomes.

#### for n in list:
- when using `for n in list`, we can read `n` from list, but cannot assign a value to `n`.
- For example: `for n in a:` `n=0`, this operation cannot be realized.
