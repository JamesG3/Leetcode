## LeetCode
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
- 142.Linked List Cycle II(find where the cycle starts `2x speed` )
- 168.Excel Sheet Column Title
- 257.Binary Tree Paths
- 394.Decode String
[d8e460d4234298930d6c3af5450af673\_hd.jpg][2]- 503.Next Greater Element II
- 77.Combinations
- 319.Bulb Switcher
- 105.Construct Binary Tree from Preorder and Inorder Traversal
- 260.Single Number III(bit manipulation)
- 318.Maximum Product of Word Lengths
- 454.4Sum II
- 477.Total Hamming Distance
- 667.Beautiful Arrangement II
- 696.Count Binary Substrings
- 544.Output Contest Matches
- 370.Range Addition
- 573.Squirrel Simulation
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
	- 364.Nested List Weight Sum II (Similar Question)
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
	- 544.Output Contest Matches
	- 541.Reverse String II

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
#### Sliding Window
- 3.Longest Substring Without Repeating Characters

#### Array and List
- **Linked List - two pointers**
	- 237.Delete Node in a Linked List
	- 141.Linked List Cycle
	- 19.Remove Nth Node From End of List
	- 83.Remove Duplicates from Sorted List
	- 203.Remove Linked List Elements
- **Construct Binary Tree**
	- 105.Construct Binary Tree from Preorder and Inorder Traversal
- **Binary Search**
	- 540.Single Element in a Sorted Array
- **Traverse & marking**
	- 448.Find All Numbers Disappeared in an Array
	- 204.Count Primes ([Sieve of Eratosthenes][3])
	- 376.Wiggle Subsequence
	- 485.Max Consecutive Ones
	- 475.Heaters
	- 203.Remove Linked List Elements
	- 167.Two Sum II - Input array is sorted
	- 525.Contiguous Array
	- 240.Search a 2D Matrix II
	- 554.Brick Wall
	- 556.Next Greater Element III
	- 531.Lonely Pixel I
- **Stack and Queue**
	- 232.Implement Queue using Stacks
	- 394.Decode String
	- 503.Next Greater Element II
	- 77.Combinations
	- 173.Binary Search Tree Iterator
	- 445.Add Two Numbers II
	- 406.Queue Reconstruction by Height
	- 526.Beautiful Arrangement
	- 484.Find Permutation
	- 20.Valid Parentheses (stack)
- **DFS**
	- 526.Beautiful Arrangement
	- 690.Employee Importance
	- 695.Max Area of Island
	- 339.Nested List Weight Sum
	- 366.Find Leaves of Binary Tree
- **Using dictionary**
	- 447.Number of Boomerangs
	- 506.Relative Ranks
	- 609.Find Duplicate File in System
	- 454.4Sum II
	- 697.Degree of an Array
	- 364.Nested List Weight Sum II
	- 362.Design Hit Counter
- **Palindrome**
	- 234.Palindrome Linked List(*O(2n)* and *O(1)* space)
	- 647.Palindromic Substrings
	- 266.Palindrome Permutation
- **Sort**
	- 280.Wiggle Sort (in-place sort)

#### deal with String
- **Using dictionary**
	- 17.Letter Combinations of a Phone Number
	- 290.Word Pattern
	- 409.Longest Palindrome
	- 451.Sort Characters By Frequency(using two lists as dictionary)
	- 609.Find Duplicate File in System
	- 676.Implement Magic Dictionary
- **Using mark/State machine**
	- 434.Number of Segments in a String
	- 500.Keyboard Row
	- 442.Find All Duplicates in an Array
	- 696.Count Binary Substrings
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
- 544.Output Contest Matches
- 370.Range Addition
- 573.Squirrel Simulation
- 338.Counting Bits
- 728.Self Dividing Numbers

#### Data Structures
- 225.Implement Stack using Queues
- 77.Combinations(using of stack)
- 445.Add Two Numbers II (stack & linked list)
- 380.Insert Delete GetRandom O(1)
- 369.Plus One Linked List (reverse the linked list)

#### DP
- 357.Count Numbers with Unique Digits
- 309.Best Time to Buy and Sell Stock with Cooldown(using state machine)
- 712.Minimum ASCII Delete Sum for Two Strings
- 70.Climbing Stairs
- 746.Min Cost Climbing Stairs
- 198.House Robber
- 256.Paint House
- 338.Counting Bits
### Marked questions
- 172.Factorial Trailing Zeroes
- Battleship in a Board: checking head horizontally and vertically.
- Binary Tree Level Order Traversal: recursive solution with a mark of level.
- Balanced Binary Tree: find maxDepth, divide and conquer.
- Invert Binary Tree: build an Invert function and a Traversal function to swap every node
- Convert Sorted Array to Binary Search Tree: insert recursively
- H-Index: how to calculate a H-Index.
	- [https://zh.wikipedia.org/wiki/H指数][4]
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
- 484.Find Permutation (stack, pointers, reverse)
- 573.Squirrel Simulation
- 712.Minimum ASCII Delete Sum for Two Strings
### Questions
- 382 Linked List Random Node: what are the test cases like? Why sometimes the result is *Wrong* when i submit a right answer?
	- **GUESS: Maybe they run a testcase for several times, and check if the output is random like (if the output is same, then the solution may be wrong)**
- 435 Non-overlapping Intervals: When i test [[1,2]() , [2,3]()] using Run Code, it pass with a result 0. However, when i click Submit Solution, the result is Wrong Answer, and it shows my result is 1, not 0. Is there someone knows whats wrong with the code or test case?
	- **Because Intervals.sort() sort this intervals by the address.**
- 142.Linked List Cycle II: why the result is the start of cycle? **MATHEMATICAL** explanation: [https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation][7]
- 36.Valid Sudoku: How to solve this using a simple solution?

[1]:	https://en.wikipedia.org/wiki/Catalan_number
[2]:	https://pic4.zhimg.com/50/d8e460d4234298930d6c3af5450af673_hd.jpg "d8e460d4234298930d6c3af5450af673_hd.jpg"
[3]:	https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
[4]:	https://zh.wikipedia.org/wiki/H%E6%8C%87%E6%95%B0
[7]:	https://discuss.leetcode.com/topic/43858/python-o-n-no-extra-space-with-mathematical-explanation