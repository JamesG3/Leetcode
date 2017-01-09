# TIPS

## ABOUT LeetCode
### List of tricky exercises
- Happy Number: *42 is an important number after experiments*
- Product of Array Except Self: from left -\> right ; then right-\>left
- Minimum Moves to Equal Array Elements: using `sum(nums) - len(nums)*min(nums)` to calculate the total moving steps  
- Arithmetic Slices: alculate the nth of 1,3,6,10... use formula `nth=n(n-1)/2`  
- 125 Valid Palindrome: cannot use a brute force solution, would cause a TLE error, should use a in place solution, use O(n).
- 189 Rotate Array: in java using reverse, only 3 times can get the result, O(n) time and O(1) space.
	- **should try in python !!**
- 96.Unique Binary Search Trees: using *Catalan number* to calculate. [https://en.wikipedia.org/wiki/Catalan\_number][1]
- 448.Find All Numbers Disappeared in an Array: reset every number, using index to represent existed/disappeared number.
- 109.Convert Sorted List to Binary Search Tree: using *fast* and *slow* to find the root of every BST; divide and conquer, recursive solution.
- 232.Implement Queue using Stacks: using 2 stack to implement Queue
- 234.Palindrome Linked List: turn **1234321** to **1231234**, then compare two parts. 
- 114.Flatten Binary Tree to Linked List **(reverse pre-order traversal)**
- 142.Linked List Cycle II(find where the cycle starts)

### Classify
#### Tree
- **Using dictionary to save every level’s nodes:** 
	- 103.Binary Tree Zigzag Level Order Traversal
	- 107.Binary Tree Level Order Traversal II
	- 199.Binary Tree Right Side View
	- 337.House Robber III
- **Tree Traversal**
	- 94.Binary Tree Inorder Traversal
	- 98.Validate Binary Search Tree
	- 144.Binary Tree Preorder Traversal
	- 145.Binary Tree Postorder Traversal
	- 230.Kth Smallest Element in a BST
	- 114.Flatten Binary Tree to Linked List (reverse pre-order traversal)
- **Greedy**
	- 121.Best Time to Buy and Sell Stock
	- 122.Best Time to Buy and Sell Stock II
- **Level traversal**
	- 116.Populating Next Right Pointers in Each Node

#### Array and List
- **Traverse the list and mark**
	- 448.Find All Numbers Disappeared in an Array
	- 204.Count Primes ([Sieve of Eratosthenes][2])
- **Stack and Queue**
	- 232.Implement Queue using Stacks
- **Palindrome**
	- 234.Palindrome Linked List(*O(2n)* and *O(1)* space)

#### deal with String
- **Using dictionary**
	- 17.Letter Combinations of a Phone Number

### Need to be refreshed
- Battleship in a Board: checking head horizontally and vertically.
- Binary Tree Level Order Traversal: recursive solution with a mark of level.
- Balanced Binary Tree: find maxDepth, divide and conquer.
- Invert Binary Tree: build an Invert function and a Traversal function to swap every node
- Convert Sorted Array to Binary Search Tree: insert recursively
- H-Index: how to calculate a H-Index.
	- [https://zh.wikipedia.org/wiki/H指数][3]
- 448.Find All Numbers Disappeared in an Array
- 120.Triangle
- 232.Implement Queue using Stacks: using 2 stack to implement Queue
- 116.Populating Next Right Pointers in Each Node
- 142.Linked List Cycle II


### Questions
- 382 Linked List Random Node: what are the test cases like? Why sometimes the result is *Wrong* when i submit a right answer?
	- **GUESS: Maybe they run a testcase for several times, and check if the output is random like (if the output is same, then the solution may be wrong)**
- 435 Non-overlapping Intervals: When i test [[1,2]() , [2,3]()] using Run Code, it pass with a result 0. However, when i click Submit Solution, the result is Wrong Answer, and it shows my result is 1, not 0. Is there someone knows whats wrong with the code or test case?
	- **Because Intervals.sort() sort this intervals by the address.**
- 142.Linked List Cycle II: why the result is the start of cycle? **MATHEMATICAL** explanation: [https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation][6]

## ABOUT PYTHON
### Useful Tools
#### [::-1]  
- For **list l**, using `l[::-1]` can return the reverse sequence of **list l**. `[::-1]` can also used in string or list like`[[1,2,3],[2,43,4],[3,4,5]]`  

#### zip  
- a=[12, 2, 3, 3, 4], b=[1, 1, 1, 1, 1], **zip(a,b)=[(12, 1), (2, 1), (3, 1), (3, 1), (4, 1)]**
- c=[(12, 1), (2, 1), (3, 1), (3, 1), (4, 1)], **`zip(*c)=[(12, 2, 3, 3, 4), (1, 1, 1, 1, 1)]`**  
	more: [http://www.cnblogs.com/BeginMan/archive/2013/03/14/2959447.html]
#### `[:]`  
- When we want to duplicate a list, we cannot simply use b=a, it will cause list *b* points to the same location. When we operate list *a*, list *b* will be modified. In other word, *b* will be always same as list *a*
- So we should use a `[:]` when creating a different list with same content.
- For example, `a=[1,2,3]`, `b=a[:]`

#### Counter  
- need to import from collection
- `from collections import Counter`
- For example: `a=['r', 'd', 'g', 'd']`, `C=Counter(a)`,      then `C=Counter({'d': 2, 'r': 1, 'g': 1})`
- Although a Counter looks like a dictionary, but it’s more flexible, we can add new element into a Counter directly, without checking if it’s exist.
- For example: `C['b']=4`, then `C=Counter({'b': 4, 'd': 2, 'r': 1, 'g': 1})`
- But we cannot do this in a dictionary.

#### Random  
- **random.randrange(stop)** same as **random.randrange(start, stop, step)**
- using for choosing a random number
- **random.sample(list, length)**
	- using for sampling from a list randomly with a certain length.

- **Exercises:**
	- 384.Shuffle an Array


#### Xrange  
- This function is very similar to range(), but returns an xrange object instead of a list.
- Save space.

#### Sort two-dimensions list OR Intervals  
- We cannot apply sort() to Intervals, it will sort it with the value of address.  
- *arr.sort(key=lambda x:x[1][7])* means sort using the first key of arr
- *arr.sort(key=lambda x:x[1][8],reverse=True)* means a reverse sort using the first key of arr
- *intervals.sort(key=lambda x:x.start)* means sort using the first key of intervals

#### iter  
- Turning a non-iterator object into a iterator object, and return the head of it.
- Including dictionary, list, string, etc.
- For example, `i = iter('example')`, the result of `print i.next()` is `e`, the second time we execute `print i.next()` will return `x`, then `a`, `m`, `p`, `l`, `e`, and an error `StopIteration`.

#### isalnum()
- `a.isalnum()`
- if a is alphanumeric characters, return True, else return False.

#### global variable
- global variable is useful especially in recursive function
- declare `global variable` under every function which may use this variable.
- For example: 230. Kth Smallest Element in a BST

#### enumerate
- can be used for getting the *index* and the *corresponding element* of a list.
- For example: `*A=["a","b"]*` is a list.  `for i,element in enumerate(a): print i; print element`
- Then we can get: `0 "a"   &    0 "b"`
- enumerate can be used in **String** and **Dictionary**
- useful to Traversal a list 

### Attentions  

#### If and while:  
- *If* is a one-time check, what is required in the *if(requirement)* can change to any value or state in the *if block*.
- For example:`a=2` `if(a<=3):` `while(a<6):` `a+=1`  
	 `return a`  
	For this part of code, the final return value would be **5**, not **3**.
	After a one-time check (a=2\<=3), the code in the *if block* can be executed, whatever the value of *a* becomes.

#### for n in list:  
- when using `for n in list`, we can read `n` from list, but cannot assign a value for `n`.
- For example: `for n in a:` `n=0`, this operation cannot be realized.

#### ASCII
- In ASCII table, ‘a’-‘z’ to “A” - “Z” is not successive.


### Simplify code:
- **root.right.next = root.next and root.next.left** equals to —- root.right.next = root.next.left **if** root.next != None

[1]:	https://en.wikipedia.org/wiki/Catalan_number
[2]:	https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
[3]:	https://zh.wikipedia.org/wiki/H%E6%8C%87%E6%95%B0
[6]:	https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation
[7]:	https://en.wikipedia.org/wiki/Catalan_number
[8]:	https://en.wikipedia.org/wiki/Catalan_number