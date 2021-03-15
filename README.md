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
Whatever code is in <code>else</code> clause will execute if the for-loop executes without `breaking`
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
The <code>ord()</code> function returns an integer representing the Unicode character (i.e., it is the inverse of the <code>chr()</code> function)
```python
print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36
```

---
### enumerate() Method
Adds a counter to an iterable and returns it in a form of enumerate object
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
Inside the placeholders we can add a <a href="https://www.w3schools.com/python/ref_string_format.asp" target="_blank"><span>formatting type</span></a> to format the results
```python
txt1 = 'My name is {fname} and I am {age}.'.format(fname='Harry Potter', age=16)
txt2 = 'My favorite professor is {0} and he is probably more than {1} years old.'.format('Albus Dumbledore', 100)
txt3 = 'My best friends are {} and {}.'.format('Hermione Granger', 'Ron Weasley')
```

---
### Lists Concatenation
The <code>extend()</code> method takes an iterable such as list, tuple, or string, and modifies the original list (it does not return any value)
```python
def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
```

---
### <code>for-else</code> List Comprehension
When using both <code>for</code> and <code>else</code> in a list comprehension, the rearrangement changes, as shown in the example below
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
A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression\
However, the power of lambda is better shown when you use them as an anonymous function inside another function, as shown <a href="https://www.w3schools.com/python/python_lambda.asp" target="_blank"><span>here</span></a>
```python
def getPoints(answers, p):
    questionPoints = lambda i, ans: (i+1)*ans - p*(not(ans))
    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res

print(getPoints([True, True, False, True], 2))    # returns 5
```
We can also <strong>sort</strong> using lambda functions, as shown in the example above
```python
def sortStudents(students):
    students.sort(key=lambda name: name.split()[-1])
    return students

students = ['John Smith', 'Jacky Mon Simonoff', 'Lucy Smith', 'Angela Zimonova']
print(sortStudents(students))
```

---
### Matrix Initialization
To declare a multidimensional list of zeroes in Python, it is necessary to use a list comprehension, as shown below
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
