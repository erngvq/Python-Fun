# Python Fun

### Interesting Methods + Swapping
<code>n</code> = number, <code>x</code> = base, <code>s</code> = string

* <code>n.bit_length()</code>
* <code>isinstance(n, int)</code>
* <code>hex(int(n, x))[2:]</code>
* <code>s.capitalilze()</code>
* <code>' '.join(s.split())</code>
* <code>a, b = b, a</code>

---
### <code>for-else</code> Loop
Whatever code is in <code>else</code> clause will execute if the for-loop executes without breaking.
```python
for i in range(0, 10, 2):
    if i % 2 == 1:
        break
    print(i)
else:
    print('else executed')
```

---
### <code>replace()</code> Method
Returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to count &rarr; <code>str.replace(old, new, count)</code>
```python
def convertTabs(code, x):
    return code.replace('\t', ''.join([' ' for i in range(x)]))
```

---
### Packing/Unpacking
```python
lst = [1, 2, 3, 4]
a, *lst, d = lst
print(a, d, lst)    # 1 4 [2, 3]
```

---
### Word Palindrome
Notice how <code>[::-1]</code> reverses the string `word`
```python
def isWordPalindrome(word):
    return word == word[::-1]
```

---
### <code>ord()</code> Function
The <code>ord()</code> function returns an integer representing the Unicode character (i.e., it is the inverse of the <code>chr()</code> function).
```python
print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36
```

---
### enumerate() Method
Adds a counter to an iterable and returns it in a form of enumerate object.
```python
lst = ['Barry', 'Allen', 'Flash']
stg = 'Zoom'
 
objlst = enumerate(lst)
objstg = enumerate(stg)

print(list(objlst))    # [(0, 'Barry'), (1, 'Allen'), (2, 'Flash')]
print(list(objstg))    # [(0, 'Z'), (1, 'o'), (2, 'o'), (3, 'm')]
```

---
### <code>format()</code> Method
Formats the specified value(s) and insert them inside the string's placeholder (defined using curly brackets)\
Inside the placeholders we can add a <a href="https://www.w3schools.com/python/ref_string_format.asp" target="_blank"><span>formatting type</span></a> to format the results.
```python
txt1 = 'My name is {fname} and I am {age}.'.format(fname='Harry Potter', age=16)
txt2 = 'My favorite professor is {0} and he is probably more than {1} years old.'.format('Albus Dumbledore', 100)
txt3 = 'My best friends are {} and {}.'.format('Hermione Granger', 'Ron Weasley')
```

---
### Lists Concatenation
The <code>extend()</code> method takes an iterable such as list, tuple, or string, and modifies the original list (it does not return any value).
```python
def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
```

---
### <code>for-else</code> List Comprehension
When using both <code>for</code> and <code>else</code> in a list comprehension, the rearrangement changes, as shown in the example below.
```python
def twoTeams(students):
    return sum([students[i] if i % 2 == 0 else students[i] * -1 for i in range(len(students))])

# Another version of this problem using slice-step-parameter
def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])
```
<a href="https://forum.freecodecamp.org/t/how-to-use-python-slice-with-the-start-stop-and-step-arguments-explained-with-examples/19202" target="_blank"><span>Python Slice Reference</span></a>

---
### <code>del</code> Keyword
The del keyword is used to delete objects, and since everything is an object in Python, the del keyword can be used to delete variables, lists, parts of a list, etc.
```python
lst = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2
del lst[k-1::k]    # deletes every second item in lst
print(lst)         # [1, 3, 5, 7]
```

---
### Lambda Functions
A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. However, the power of lambda is better shown when you use them as an anonymous function inside another function, as shown <a href="https://www.w3schools.com/python/python_lambda.asp" target="_blank"><span>here</span></a>.
```python
def getPoints(answers, p):
    questionPoints = lambda i, ans: (i+1)*ans - p*(not(ans))
    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res

print(getPoints([True, True, False, True], 2))    # returns 5
```
We can also <strong>sort</strong> using lambda functions, as shown in the following example.
```python
def sortStudents(students):
    students.sort(key=lambda name: name.split()[-1])
    return students

students = ['John Smith', 'Jacky Mon Simonoff', 'Lucy Smith', 'Angela Zimonova']
print(sortStudents(students))
```

---
### Matrix Initialization
To declare a multidimensional list of zeroes in Python, it is necessary to use a list comprehension, as shown below.
```python
m = 3
matrix = [[0 for i in range(m)] for j in range(m)]
```

---
### Weighted Alphabet Dictionary
```python
# ASCII value of uppercase alphabets: [65:91)
# ASCII value of lowercase alphabets: [97:123)

alphabet = dict([(chr(i), i-96) for i in range(97, 123)])
```

---
### Zip Zip Zip
The <code>zip()</code> function takes iterables (can be zero or more), aggregates them in a tuple, and returns them.
```python
# Mathching ith item of one list with ith item of another list
team1 = ['Jane', 'Bob', 'Peter']
team2 = ['Oscar', 'Lidia', 'Ann']
print([[team1[i], team2[i]] for i in range(len(team1))])    # [['Jane', 'Oscar'], ['Bob', 'Lidia'], ['Peter', 'Ann']]

# Using zip()
print(list(zip(team1, team2)))                              # [('Jane', 'Oscar'), ('Bob', 'Lidia'), ('Peter', 'Ann')]

# Using zip() powerfully
team3 = ['Harry', 'Hermione']
print(list(zip(team1, team2, team3)))                       # [('Jane', 'Oscar', 'Harry'), ('Bob', 'Lidia', 'Hermione')]
```
Given two lists containing nucleotide bases, use the power of the <code>zip()</code> function to write a helper routine that returns those elements in the <code>ith</code> position of first list that match their complement in the  <code>ith</code> position of the second list.
```python
complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
def groupIfDiff(lst1, lst2):
    return [x for x, y in zip(lst1, lst2) if complement[x] == y]
print(groupIfDiff(['A', 'C', 'G', 'C', 'A', 'T'], ['T', 'A', 'G', 'G', 'C', 'A']))    # returns ['A', 'C', 'T']
```
---
### Map, Filter, Reduce
The <code>map()</code> function returns a map object (which is an iterator) of the results after applying the given function to each item of a given iterable.
```python
# This script strips the last digit of each integer in the given list
lst = [42, 239, 365, 50]
def fix(x):
    return x // 10
print(list(map(fix, result)))    # returns [4, 23, 36, 5]
```
The <code>filter()</code> function filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
```python
# This script filters out those courses whose lengths are seven
courses = ['Art', 'Finance', 'Business', 'Speech', 'History', 'Writing', 'Statistics']
def consider(course):
    return len(course) < 7
print(list(filter(consider, courses)))    # returns ['Art', 'Speech']
```
The <code>reduce()</code> function is used to apply a particular function (first argument) to all of the list elements in the sequence (second argument).
```python
# This script finds the least common denominator for the given list
from fractions import gcd
denominators = [2, 3, 4, 5, 6]

# In order to use reduce(), the functools module must be invoked
print(functools.reduce(lambda a, b: a * b / gcd(a, b), denominators))    # returns 60
```

---
### Counter Class
Special type of object data-set (provided with the collections module in Python3) which is used to count hashable objects.
```python
from collections import Counter
text = '$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ'
print(Counter(text).most_common(1)[0][0])    # returns C
```

---
### Prime Numbers Logic
Prime numbers are numbers that only have two factors: 1 and themselves. Therefore, when checking if an arbitrary number <code>n</code> is prime, we can say that <code>n = ab</code>, where <code>a <= b</code>. As such, <code>aa <= ab = n</code>, meaning that we can iterate up to <img src="https://latex.codecogs.com/svg.latex?\sqrt{n}" /> numbers (starting from 2) when checking if the number is prime via the modulo operator. Note that the code below uses this logic to find all the prime numbers in the range <code>[x, y)</code> and them sum them up. 
```python
def primesSum(x, y):
    return sum([n for n in range(max(2, x), y + 1) if not 0 in [n % i for i in range(2, int(n**0.5+1))]])
```

---
### <code>iter()</code> Function
Creates an object which can be iterated one element at a time, which is useful when coupled with loops.
```python
def calcFinalScore(scores, n):
    gen = iter(sorted([i**2 for i in scores], reverse=True))
    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5
    return res
```

---
### Fibonacci Generator
```python
import functools
def fibonacciGenerator(n):
    return functools.reduce(lambda a, b: a + [a[-1] + a[-2]], range(n-2), [0, 1])

print(fibonacciGenerator(12))    # returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
