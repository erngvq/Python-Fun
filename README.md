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
<pre>
for i in range(0, 10, 2):
    if i % 2 == 1:
        break
    print(i)
else:
    print('else executed')
</pre>

---
### <code>replace()</code> Method
Returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to count &rarr; <code>str.replace(old, new, count)</code>
<pre>
def convertTabs(code, x):
    return code.replace('\t', ''.join([' ' for i in range(x)]))
</pre>

---
### Packing/Unpacking
<pre>
lst = [1, 2, 3, 4]
a, *lst, d = lst
print(a, d, lst)    # 1 4 [2, 3]
</pre>

---
### Word Palindrome
Notice how <code>[::-1]</code> reverses the string `word`
<pre>
def isWordPalindrome(word):
    return word == word[::-1]
</pre>

---
### <code>ord()</code> Function
The <code>ord()</code> function returns an integer representing the Unicode character (i.e., it is the inverse of the <code>chr()</code> function)
<pre>
print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36
</pre>

---
### enumerate() Method
Adds a counter to an iterable and returns it in a form of enumerate object
<pre>
lst = ['Barry', 'Allen', 'Flash']
stg = 'Zoom'
 
objlst = enumerate(lst)
objstg = enumerate(stg)

print(list(objlst))    # [(0, 'Barry'), (1, 'Allen'), (2, 'Flash')]
print(list(objstg))    # [(0, 'Z'), (1, 'o'), (2, 'o'), (3, 'm')]
</pre>

---
### <code>format()</code> Method
Formats the specified value(s) and insert them inside the string's placeholder (defined using curly brackets)\
Inside the placeholders we can add a <a href="https://www.w3schools.com/python/ref_string_format.asp" target="_blank"><span>formatting type</span></a> to format the results
<pre>
txt1 = 'My name is {fname} and I am {age}.'.format(fname='Harry Potter', age=16)
txt2 = 'My favorite professor is {0} and he is probably more than {1} years old.'.format('Albus Dumbledore', 100)
txt3 = 'My best friends are {} and {}.'.format('Hermione Granger', 'Ron Weasley')
</pre>

---
### Lists Concatenation
The <code>extend()</code> method takes an iterable such as list, tuple, or string, and modifies the original list (it does not return any value)
<pre>
def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
</pre>

---
### <code>for-else</code> List Comprehension
When using both <code>for</code> and <code>else</code> in a list comprehension, the rearrangement changes
<pre>
def twoTeams(students):
    return sum([students[i] if i % 2 == 0 else students[i] * -1 for i in range(len(students))])
</pre>
