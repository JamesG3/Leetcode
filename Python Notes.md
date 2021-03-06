## ABOUT PYTHON
### Useful Tools
#### `[::-1]`  
- For **list l**, using `l[::-1]` can return the reverse sequence of **list l**. `[::-1]` can also used in string or list like`[[1,2,3],[2,43,4],[3,4,5]]`
#### Another way to reverse a List/string
- `For item in reversed(L):    print item`

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
- *arr.sort(key=lambda x:x[1][1])* means sort using the first key of arr
- *arr.sort(key=lambda x:x[1][2],reverse=True)* means a reverse sort using the first key of arr
- *intervals.sort(key=lambda x:x.start)* means sort using the first key of intervals
#### sorted() function
- Want to sort a integer list `L` Lexicographically? 
	- `sorted(L, key = str)`
#### iter  
- Turning a non-iterator object into a iterator object, and return the head of it.
- Including dictionary, list, string, etc.
- For example, `i = iter('example')`, the result of `print i.next()` is `e`, the second time we execute `print i.next()` will return `x`, then `a`, `m`, `p`, `l`, `e`, and an error `StopIteration`.

#### isalnum()
- `a.isalnum()`
- if a is alphanumeric characters, return True, else return False.
#### divmod()
- divmoid(m, n) returns a tuple (m/n, m%10)
- e.g. divmoid(342, 10)   \>\>    (34, 2)
- e.g. Leetcode 728

#### enumerate (useful generator)
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
	- **switch**
		- `def dispatch_dict(operator, x, y):`
			`return {`
			`'add': lambda: x + y,`
			`'sub': lambda: x - y,`
			`'mul': lambda: x * y,`
			`'div': lambda: x / y,`
			`}.get(operator, lambda: None)()`
		- `dispatch_dict('mul', 2, 8)`   -\>   16
		- `dispatch_dict('unknown', 2, 8)`  -\>  None

- sort a dictionary by value
	- `dic = {'a': 4, 'b': 3, 'c': 2, 'd': 1}`
	- `sorted(dic.items(), key=lambda x: x[1])`
	- get: `[('d', 1), ('c', 2), ('b', 3), ('a', 4)]`
- sort a list by self defined comparison function
	- Using **cmp**
	- `l = ['12', '34', '1', '96', '30']`
	- `sorted(nums, cmp = lambda x, y: 1 if x+y < y+x else -1)`
	- `['96', '34', '30', '12', '1']`
	- See Leetcode Question: _179. Largest Number_

#### regex (Regular expression)
- **Search pattern** example:[https://github.com/JamesG3/HackerRank/blob/master/String/HackerRank%20in%20a%20String!.py][3]
- More information: [https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html][4]
#### dictionary
- **dic.values**
	- for a dictionary, we can use `for x in dic.values()` to traverse all values for each key:value pairs.
- merge two dictionaries:
	- `z = dict(x, **y)`
- `dict.get(key, 0)` If key in dict, return the key’s value, if not, return 0.
#### partition function
- for a string `S = ‘abc&def’`, using `S.partition(‘&’)`, we can get `[abc, &, def]`
#### schedule
- run Python functions (or any other callable) periodically.[https://schedule.readthedocs.io/en/stable/?\_\_s=qfsmdzfwpufq4vxscpre][5]
- `schedule.every(10).minutes.do(myfunc)`
#### namedtuples
- to defining class manually
- Like tuples, namedtuples are immutable.
- `from collections import namedtuple`
	`Car = namedtup1e('Car', 'color mileage')`
	`my_car = Car('red', 3812.4)`
	`my_car.color`   \>\>   `red`
	`my_car.mileage`   \>\>   `3812.4 `

#### unpack operator for tuple and dict
- `def myfunc(x, y, z):`
	`print(x, y, z)`
	`tuple_vec = (1, 0, 1)`
	`dict_vec = {'x': 1, 'y': 0, 'z': 1}`
	`myfunc(*tuple_vec)` \>\> (1, 0, 1)
	`myfunc(*dict_vec)` \>\> (‘x’, ‘y’, ‘z’)
	`myfunc(**dict_vec)` \>\> (1, 0, 1)
- Because the dict has ”random” order, using dict value unpack operator usually comes with key matching, which is `myfunc(*dict_vec)`

#### List Comprehensions:
- `(values) = [(expression) for (value) in (collection)]`
- Eg. `[x**2 for x in xrange(5)]`  -\> `[0,1,4,9,16]`
**Filtering**
- `[(expression) for (value) in (collection) if (condition)]`
- E.g. `[x**2 for x in xrange(5) if x%2 == 0]` -\> `[0,4,16]`

#### `__str__`:
- Usually is mainly used in giving an easy representation of a class.
- In class `A`, write a function called `__str__(self)`, return something
- Then call `print A` to get that representation.
#### `__repr__`
- Usually should be unambiguous
- Similar with `__str__`, but the representation can be shown by calling the `class’s name`
	class Car:
		    def __init__(self, color, mileage):
		        self.color = color
		        self.mileage = mileage
		def __repr__(self):
		        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)
		def __str__(self):
		        return '{self.__class__.__name__}({self.color})'.format(self=self)
		
		mycar = Car('red', 3223)
		mycar / repr(mycar)       -> gets Car(red, 3223)
		str(mycar) / print mycar  -> gets Car(red)
#### Switch-case emulating
	def calculate(operator, x, y):
	        return{
	            'add': lambda: x+y,
	            'sub': lambda" x-y,
	            'mul': lambda: x*y,
	            'div': labmbda:x/y,
	        }.get(operator, lambda: None)()
- use dictionary to simulate Switch
- If operator doesn’t exist, return None
#### Finding the most common elements in an iteration
	import collections
	c = collections.Counter('hithere')
	c    ->     Counter({'h':2, 'i':1, 't':1, 'r':1, 'e':2})
	c.most_common(2)   ->    [('h', 2), ('e', 2)]


#### permutations
	import itertools
	for p in itertools.permutations('123'):
	    print p
	>> ('1', '2', '3')
	>> ('1', '3', '2')
	>> ('2', '1', '3')
	>> ('2', '3', '1')
	>> ('3', '1', '2')
	>> ('3', '2', '1')

#### arg and kwargs
	def foo(required, *args, **kwargs):
	        print required
	        if args:
	            print args
	        if kwargs:
	            print kwargs
	foo('hi')               >>           hi
	foo('hi',1,2,3)         >>           hi       tuple(1,2,3)
	foo('hi',1,2, key1 = 'w', key2 = '4')
	>> hi    (1,2)    {'key1':'w', 'key2':'4'}

- can be used to override a class / wrap a function and forward arguments
		class Car:
		    def __init__(self, color, mileage):
		        self.color = color
		        self.mileage = mileage
		
		class AlwaysBlueCar(Car):
		    def __init__(self, *args, **kwargs):
		        super().__init__(*args, **kwargs)
		        self.color = 'blue'

#### virtual environment
- `which pip`/`which pip3` tells where the models are installed
- `python3 -m venv ./venv` creates a folder with python packages under current path.
- `source ./venv/bin/activate` activates the virtual environment.
- then the result of `which pip3/pip` turns into `./venv/bin/pip or pip3`
- `pip3 list` list all the installed modules in venv.
- `deactivate` to deactivate the virtual environment.
#### globals() and locals()
- Calling these two function can return a dict which includes all global/local variables in the current scope.


#### else branch for ‘for’ and ‘while’ loop
- Python’s **‘for’** and **‘while’** loops support an **‘else’** clause that executes only if the loops terminates without hitting a ‘break’ statement.
	def contains(haystack, needle):
		for item in haystack:
		    if item == needle:
		        break
		else:
		    raise ValueError('Needle not found')



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
- python list can even contain functions: `def func(a,b): return a+b`, `A=[func]`, `A[0](2,4)` -\> get 6

#### Python's built-in HTTP server
- Python3: `python3 -m http.server`
- Python2: `python -m SimpleHTTPServer 8000`

### Simplify code:
- **root.right.next = root.next and root.next.left** equals to —\> root.right.next = root.next.left **if** root.next != None
- **`ar = [int(i) for i in raw_input().strip().split()]`**
	convert the input **2 4 6 8 3** to `[2,3,6,8,3]`
- Find the highest ‘price’ in a dic: **`max_price = max(item['price'] for item in dict_list)`**
- Delete all ’s’ in a string S=’ssdwedSdfag’ :
	**S.replace('-','')**
- For a dictionary `dic = {a:[1,2,3],b:[6],c:[4,6]}`, print all values if the length of list larger than 1.
	`print [x for x in dic.values() if len(x)>1] `
- Another example: [https://github.com/JamesG3/HackerRank/blob/master/Implementation/Cut%20the%20sticks.py][6]
- Check flag or truthiness: 
	- `x, y, z = 0, 1, 0`
	- `if any((x, y, z))` == `if 1 in (x, y, z) ` == `if x or y or z`
- `dict.get(key, 0)` If key in dict, return the key’s value, if not, return 0. `dict[key] = dict.get(key, 0) + 1`

[1]:	https://en.wikipedia.org/wiki/Catalan_number
[2]:	https://en.wikipedia.org/wiki/Catalan_number
[3]:	https://github.com/JamesG3/HackerRank/blob/master/String/HackerRank%20in%20a%20String!.py
[4]:	https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
[5]:	https://schedule.readthedocs.io/en/stable/?__s=qfsmdzfwpufq4vxscpre
[6]:	https://github.com/JamesG3/HackerRank/blob/master/Implementation/Cut%20the%20sticks.py