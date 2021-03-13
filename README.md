# Python Fun

### Interesting Methods + Swapping
<code>n</code> = number
<code>x</code> = base

* <code>n.bit_length()</code>
* <code>isinstance(n, int)</code>
* <code>hex(int(n, x))[2:]</code>
* <code>a, b = b, a</code>

### replace() Method
Returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to count &rarr; <code>str.replace(old, new, count)</code>
<pre>
def convertTabs(code, x):
    return code.replace('\t', ''.join([' ' for i in range(x)]))
</pre>

### Word Palindrome
Notice how <code>[::-1]</code> reverses the string `word`
<pre>
def isWordPalindrome(word):
    return word == word[::-1]
</pre>

### <code>ord()</code> Function
The <code>ord()</code> function returns an integer representing the Unicode character (i.e., it is the inverse of the <code>chr()</code> function)
<pre>
print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36
</pre>

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

### <code>format()</code> Method
Formats the specified value(s) and insert them inside the string's placeholder (defined using curly brackets)\
Inside the placeholders we can add a <a href="https://www.w3schools.com/python/ref_string_format.asp" target="_blank"><span>formatting type</span></a> to format the results
<pre>
txt1 = 'My name is {fname} and I am {age}.'.format(fname='Harry Potter', age=16)
txt2 = 'My favorite professor is {0} and he is probably more than {1} years old.'.format('Albus Dumbledore', 100)
txt3 = 'My best friends are {} and {}.'.format('Hermione Granger', 'Ron Weasley')
</pre>
