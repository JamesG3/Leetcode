# TIPS

## ABOUT LeetCode
### List of tricky exercises
- 172.Factorial Trailing Zeroes
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
- 168.Excel Sheet Column Title
- 257.Binary Tree Paths
- 394.Decode String
- 503.Next Greater Element II
- 77.Combinations
- 319.Bulb Switcher
- 105.Construct Binary Tree from Preorder and Inorder Traversal
- 260.Single Number III(bit manipulation)
- 318.Maximum Product of Word Lengths
- 454.4Sum II
- 477.Total Hamming Distance
- 667.Beautiful Arrangement II
### Classify
#### Tree
- **Using dictionary to save every level’s nodes:** 
	- 103.Binary Tree Zigzag Level Order Traversal
	- 107.Binary Tree Level Order Traversal II
	- 199.Binary Tree Right Side View
	- 337.House Robber III
	- 501.Find Mode in Binary Search Tree
	- 508.Most Frequent Subtree Sum
	- 513.Find Bottom Left Tree Value
	- 515.Find Largest Value in Each Tree Row
- **BFS**
	- 637.Average of Levels in Binary Tree
- **Level traversal**
	- 116.Populating Next Right Pointers in Each Node
- **Binary Search Tree**
	- 669.Trim a Binary Search Tree
	- 501.Find Mode in Binary Search Tree
- **Tree Traversal**
	- 94.Binary Tree Inorder Traversal
	- 98.Validate Binary Search Tree
	- 144.Binary Tree Preorder Traversal
	- 145.Binary Tree Postorder Traversal
	- 230.Kth Smallest Element in a BST
	- 114.Flatten Binary Tree to Linked List (reverse pre-order traversal)
	- 501.Find Mode in Binary Search Tree
	- 508.Most Frequent Subtree Sum
	- 530.Minimum Absolute Difference in BST
	- 543.Diameter of Binary Tree
	- 538.Convert BST to Greater Tree
	- 617.Merge Two Binary Trees
	- 655.Print Binary Tree
- **recursive**
	- 257.Binary Tree Paths
	- 129.Sum Root to Leaf Numbers
	- 508.Most Frequent Subtree Sum
	- 617.dMerge Two Binary Trees
- **Global variable**
	- 129.Sum Root to Leaf Numbers
- **concepts about tree**
	- 331.Verify Preorder Serialization of a Binary Tree
	- 173.Binary Search Tree Iterator

#### Greedy
- 121.Best Time to Buy and Sell Stock
- 122.Best Time to Buy and Sell Stock II
- 475.Heaters
- 198.House Robber
- 213.House Robber II
- 334.Increasing Triplet Subsequence

#### Array and List
- **Construct Binary Tree**
	- 105.Construct Binary Tree from Preorder and Inorder Traversal
- **Binary Search**
	- 540.Single Element in a Sorted Array
- **Traverse the list and mark**
	- 448.Find All Numbers Disappeared in an Array
	- 204.Count Primes ([Sieve of Eratosthenes][2])
	- 376.Wiggle Subsequence
	- 485.Max Consecutive Ones
	- 475.Heaters
	- 203.Remove Linked List Elements
	- 167.Two Sum II - Input array is sorted
	- 525.Contiguous Array
	- 240.Search a 2D Matrix II
	- 554.Brick Wall
	- 556.Next Greater Element III
- **Stack and Queue**
	- 232.Implement Queue using Stacks
	- 394.Decode String
	- 503.Next Greater Element II
	- 77.Combinations
	- 173.Binary Search Tree Iterator
	- 445.Add Two Numbers II
	- 406.Queue Reconstruction by Height
	- 526.Beautiful Arrangement
- **DFS**
	- 526.Beautiful Arrangement
	- 690.Employee Importance
	- 695.Max Area of Island
- **Using dictionary**
	- 447.Number of Boomerangs
	- 506.Relative Ranks
	- 609.Find Duplicate File in System
	- 454.4Sum II
- **Palindrome**
	- 234.Palindrome Linked List(*O(2n)* and *O(1)* space)
	- 647.Palindromic Substrings


#### deal with String
- **Using dictionary**
	- 17.Letter Combinations of a Phone Number
	- 290.Word Pattern
	- 409.Longest Palindrome
	- 451.Sort Characters By Frequency(using two lists as dictionary)
	- 609.Find Duplicate File in System
	- 676.Implement Magic Dictionary
- **Using mark**
	- 434.Number of Segments in a String
	- 500.Keyboard Row
	- 442.Find All Duplicates in an Array
- **Others**
	- 461.Hamming Distance
	- 482.License Key Formatting
	- 481.Magical String
#### Simulation
- 498.Diagonal Traverse
- 495.Teemo Attacking
#### HASH
- 535.Encode and Decode TinyURL
- 347.Top K Frequent Elements
#### Mathematics
- 172.Factorial Trailing Zeroes
- 168.Excel Sheet Column Title
- 476.Number Complement
- 171.Excel Sheet Column Number
- 492.Construct the Rectangle
- 504.Base 7
- 319.Bulb Switcher
- 260.Single Number III(bit manipulation)
- 343.Integer Break
- 357.Count Numbers with Unique Digits
- 318.Maximum Product of Word Lengths(Bit Map)
- 553.Optimal Division
- 462.Minimum Moves to Equal Array Elements II
- 477.Total Hamming Distance
#### Data Structures
- 225.Implement Stack using Queues
- 77.Combinations(using of stack)
- 445.Add Two Numbers II (stack & linked list)
- 380.Insert Delete GetRandom O(1)
#### DP
- 357.Count Numbers with Unique Digits
- 309.Best Time to Buy and Sell Stock with Cooldown(using state machine)
### Need to be refreshed
- 172.Factorial Trailing Zeroes
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
- 168.Excel Sheet Column Title
- 198.House Robber: Greddy
- 257.Binary Tree Paths: Nice Grammar!!
- 394.Decode String: using stack
- 506.Relative Ranks(version: same score supported)
- 334.Increasing Triplet Subsequence
- 503.Next Greater Element II
- 160.Intersection of Two Linked Lists
- 77.Combinations
- 173.Binary Search Tree Iterator
- 319.Bulb Switcher
- 105.Construct Binary Tree from Preorder and Inorder Traversal
- 260.Single Number III(bit manipulation)
- 357.Count Numbers with Unique Digits
- 318.Maximum Product of Word Lengths
- 309.Best Time to Buy and Sell Stock with Cooldown
- 477.Total Hamming Distance
- 667.Beautiful Arrangement II
### Questions
- 382 Linked List Random Node: what are the test cases like? Why sometimes the result is *Wrong* when i submit a right answer?
	- **GUESS: Maybe they run a testcase for several times, and check if the output is random like (if the output is same, then the solution may be wrong)**
- 435 Non-overlapping Intervals: When i test [[1,2]() , [2,3]()] using Run Code, it pass with a result 0. However, when i click Submit Solution, the result is Wrong Answer, and it shows my result is 1, not 0. Is there someone knows whats wrong with the code or test case?
	- **Because Intervals.sort() sort this intervals by the address.**
- 142.Linked List Cycle II: why the result is the start of cycle? **MATHEMATICAL** explanation: [https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation][6]
- 36.Valid Sudoku: How to solve this using a simple solution?

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
	- 380.Insert Delete GetRandom O(1)


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
#### lambda:
- lambda is a anonymous function. For example: **`a = lambda x:x+1`**, then **a(1)** is **1+1=2**. Same as **`def a(x): return x+1`**
- variable before colon is the input of a function, after colon is the return value.
- tools for lambda:
	- `foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]`
	- **filter**
		- `print filter(lambda x: x % 3 == 0, foo)`
		- `[18, 9, 24, 12, 27]`
	- **map**
		- `print map(lambda x: x * 2 + 10, foo)`
		- `[14, 46, 28, 54, 44, 58, 26, 34, 64]`
	- **reduce**
		- `print reduce(lambda x, y: x + y, foo)`
		- `139`
#### regex (Regular expression)
- **Search pattern** example:[https://github.com/JamesG3/HackerRank/blob/master/String/HackerRank%20in%20a%20String!.py][9]
- More information: [https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html][10]
#### dic.values
- for a dictionary, we can use `for x in dic.values()` to traverse all values for each key:value pairs.
#### partition function
- for a string `S = ‘abc&def’`, using `S.partition(‘&’)`, we can get `[abc, &, def]`


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

#### Python list `[]`:
- python list can contain multiple types of elements
- example: `[1,'a',[1,2,3],{3:'r'}]`

### Simplify code:
- **root.right.next = root.next and root.next.left** equals to —\> root.right.next = root.next.left **if** root.next != None
- **`ar = [int(i) for i in raw_input().strip().split()]`**
	convert the input **2 4 6 8 3** to `[2,3,6,8,3]`
- Find the highest ‘price’ in a dic: **`max_price = max(item['price'] for item in dict_list)`**
- Delete all ’s’ in a string S=’ssdwedSdfag’ :
	**S.replace('-','')**
- For a dictionary `dic = {a:[1,2,3],b:[6],c:[4,6]}`, print all values if the length of list larger than 1.
	`print [x for x in dic.values() if len(x)>1] `
- Another example: [https://github.com/JamesG3/HackerRank/blob/master/Implementation/Cut%20the%20sticks.py][11]


[1]:	https://en.wikipedia.org/wiki/Catalan_number
[2]:	https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
[3]:	https://zh.wikipedia.org/wiki/H%E6%8C%87%E6%95%B0
[6]:	https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation
[7]:	https://en.wikipedia.org/wiki/Catalan_number
[8]:	https://en.wikipedia.org/wiki/Catalan_number
[9]:	https://github.com/JamesG3/HackerRank/blob/master/String/HackerRank%20in%20a%20String!.py
[10]:	https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
[11]:	https://github.com/JamesG3/HackerRank/blob/master/Implementation/Cut%20the%20sticks.py