---
jupyter:
  jupytext:
    formats: ipynb,py:light,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Variables & types

```python
var = 10
print(var)
print(var + 1)
```

```python
# Variable names are case-sensitive!
Var = 11
print(var)
print(Var)
```

```python
# Valid names
x = 5
some_variable_name55 = 'hello'
NotByTheConventionsButStillValid = 3.14

print(NotByTheConventionsButStillValid + x)
print(x * some_variable_name55)
```

```python
# Some invalid names
2morrow = 'Wednesday'
variable! = '!'
```

```python
a, b, c = 1, 2, 3
print(a + b + c)
a = 9
print(a + b + c)
```

```python
a, b, c = 1, 2, 3, 4
a, b, c = 1, 2
```

```python
_, x, y, _ = 1, 2, 3, 4
print(x, y)
print(_)
```

```python
print(x)
print(type(x))
```

```python
print(type(4), type(3.14), type('some string'))
```

```python
t = type(x)
print(type(t))
```

```python
print(type(type(t)))
print(type(t) == type(type(t)))
```

```python
a = None
print(a)
print(type(a))
print(type(type(a)))
```

```python
# Booleans

a = 5
b = 3

print(a == b) # False
print(a == b + 2) # True
print(a != b) # True

print('*' * 20)

print(a > b) # True
print(a > a) # False
print(a >= a) # True
print(a < b) # False
print(a <= b) # False
```

```python
condition = (a > b)
print(condition)
print(type(condition))
```

```python
condition1, condition2 = True, False
print(condition1, condition2)
```

```python
print((5 > 3) and (2 > 3)) # True and False = False
print((5 > 3) or (2 > 3)) # True or False = True
print(not (5 > 3)) # not True = False
print(not False) # True
```

```python
print(3 == '3') # False
print(3 != '3') # True
print(3 == 3.0) # True
print(3 == None) # False
```

```python
print(3 > '3') # Not supported in Python 3, False in Python 2
```

```python
# For numbers: 0 is treated as False, all other (non-zero) numbers as True
print(bool(1)) # True
print(bool(51512)) # True
print(bool(0)) # False
print(bool(0.0000000001)) # True

# For strings: an empty string is treated as False, non-empty strings as True
print(bool('0')) # True
print(bool('')) # False

# None is treatd as False
print(bool(None)) # False
```

```python
# This is a comment

'''
This is
a long
comment.
'''

"""
Also this.
"""
```

```python
# Commented out code

# print(5 + 3)
# print(5 - 3)
```

# Numbers

```python
x = 2
y = 2.71828182846
print(type(x), type(y))
print(x + y)
```

```python
print(5 / 2) # Different in Python 2, unless: from __future__ import division
print(5 // 2)
print(4 / 2)
```

```python
print(5 / 0)
```

```python
print(5 % 3)
```

```python
print(5 ** 2712)
```

```python
print(5.0 ** 2712.0)
```

```python
print(5.0 ** 123.0)
print(5.0 ** -123.0)
print(4e05)
print(4e-03)
print(1e06 == 10 ** 6)
print(10e06 == 10 ** 6)
```

```python
print(3.14 ** 2.71)
print((-3.14) ** 2.71) # Results a complex number in Python 3
```

```python
print(2 * 3 + 4) # 6 + 4 = 10
print(2 * (3 + 4)) # 2 *  7 = 14
print((2 * 3) + 4) # 6 + 4 = 10
```

```python
x = int('5')
y = float('7.7')
print(x, y, x + y)
print(float('5'))
```

```python
print(int('7.7'))
```

```python
print(int(float('7.7')))
```

```python
print(int(True), int(False), float(True), float(False))
```

```python
print(int(bool(5)))
```

```python
x = 5
x += 5 # 10
print(x)

x -= 3 # 7
print(x)

x *= 5 # 35
print(x)

x //= 5 # 7
print(x)

x /= 6
print(x)

x **= 6
print(x)
```

# Strings

```python
s1 = 'This is a string'
s2 = "This is also a string"
print(s1)
print(s2)
print(s1 + '. ' + s2 + '.')
```

```python
# Special chars
print('### Title ###\na:\t5\nb:\t6')
```

```python
# Escaping
print('### Title ###\\na:\\t5\\nb:\\t6')
```

```python
print(r'### Title ###\na:\t5\nb:\t6')
```

```python
print('Don\'t', "Don't")
```

```python
print(8 * 'cat ')
print('cat ' * 8)
```

```python
text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(text)
print(len(text))
print(type(len(text)))
```

```python
print(text[0])
print(text[4])
print(text[-1])
print(text[-4])
print(type(text[0]))
```

```python
print(text[0:5])
print(text[7:-7])
print(text[7:])
print(text[:-7])
print(text[:3])
```

```python
print(text[0:10:3])
print(text[:10:3])
print(text[::3])
print(text[::-3])
```

```python
print(text[::-1])
```

```python
s1 = str(5)
s2 = str(5.0)
print(s1 + '\n' + s2 + '\n')
print(str(6 > 3))
```

```python
s = 'text'
print(s)
print(str(s))
print(s == str(s))
```

```python
print(repr(s))
print(s == repr(s))
```

```python
s
```

```python
s += ' 123\t'
print(s)

s *= 3
print(s)
```

```python
very_long_string = 'This is a very very very long string and there is no problem with that, but we will have to break it ' + \
        'such that it will extend to more than one line'
print(very_long_string)
```

```python
very_long_string = '''This is another very long string.
This one really goes down to more than one line.
Every new line here really becomes a new line.'''

print(very_long_string)
```

```python
string = 'An elephant'
substring = 'n el'
contained = substring in string
print(contained)
```

# Conditions & loops

```python
a = 6
b = 4

if a > b:
    print('a > b')
else:
    print('a < b')
```

```python
# Indentation in Python is MUST

if 5 > 3:
print('...')
```

```python
if 5 > 3:
    print('Ok')
    if 5 > 3:
     print('Not recommended!')
```

```python
# So are colons
if 5 > 3
    print('Error')
```

```python
condition1 = a > b
condition2 = a > b + 3
print(condition1, condition2)

if condition1:
    print('a > b')
    
if condition2:
    print('a > b + 3')
    
if condition1 == True:
    print('There is no reason to compare a boolean variable to True.')
```

```python
if a > b + 3:
    print('a > b + 3')
    
if a > b + 2:
    print('a > b + 2')
    
if a > b + 1:
    print('a > b + 1')
    
if a > b:
    print('a > b')
```

```python
if a > b + 3:
    print('a > b + 3')
elif a > b + 2:
    print('a > b + 2')
elif a > b + 1:
    print('a > b + 1')
elif a > b:
    print('a > b')
else:
    print('a <= b')
```

```python
if a > b:
    if a > b * 2:
        print('a >> b')
    else:
        print('a > b but not a >> b')
else:
    print('a <= b')
    
print('*' * 20)
    
if a > b and a > b * 2:
    print('a >> b')
elif a > b and not a > b * 2:
    print('a > b but not a >> b')
else:
    print('a <= b')
```

```python
for s in 'some string':
    print(s)
```

```python
dna = 'AAAATCTTGAGATTCGATATGGGA'
A_count = 0

for nt in dna:
    if nt == 'A':
        A_count += 1
        
print(A_count)
```

```python
print(dna.count('A'))
print(dna.count('AT'))
```

```python
A_count = 0
i = 0

while i < len(dna):
    
    if dna[i] == 'A':
        A_count += 1
    
    i += 1
    
print(A_count)
print(i, len(dna))
```

```python
import random

synthesized_dna = ''
synthesized_A = 0

while synthesized_A < 9:

    r = random.randint(0, 4)

    if r == 0:
        synthesized_dna += 'A'
        synthesized_A += 1
    elif r == 1:
        synthesized_dna += 'C'
    elif r == 2:
        synthesized_dna += 'G'
    else: # (r == 3)
        synthesized_dna += 'T'
        
print(synthesized_dna)
print(synthesized_dna.count('A'))
```

```python
# while loops are dangerous (they may result infinite loops)

import time

i = 0

while True:
    i += 1
    print(i)
    # That's actually a very important trick for slowing down infinite loops
    time.sleep(0.5)
```

```python
for s in 'ABCDEFGHIJK':
    
    if s == 'D':
        continue
    elif s == 'I':
        break
    else: # Not really necessary.
        pass
    
    print(s)
```

```python
for s1 in 'ABC':
    for s2 in '123':
        
        print(s1 + s2)
        
        if s1 == 'A' and s2 == '2':
            break # Will only affect innermost loop
```

# Lists, tuples, dictionaries & sets

```python
l = [1, 2, 3, 'a', 4, 5]
print(l)
print(type(l))
print(len(l))
print(l[1], l[3])
```

```python
print([1, 2, [1, 2]])
print([1, 2, [1, 2, [1, 2]]])
```

```python
a = [1, 2, 3]
a.append(4)
print(a)

a += [5]
print(a)

a += [6, 7]
print(a)

a.extend([8, 9])
print(a)

a.append([10, 11])
a.append([12])
print(a)
```

```python
l = [1, 2, 3, 4]
l.append(l)
print(l)
print(l[4])
print(l == l[4])
print(l[4][2])
print(l[4][4][4][4][4][4][4][4][2])
```

```python
a += 7
```

```python
a += [11, 12, 13]
print(a)

a += a
print(a)
```

```python
a = [1, 2, 3]
print(a * 3)
a *= 3
print(a)
```

```python
print(a[3:8])
print(a[::-1])
```

```python
bases = list('ACGT')
print(bases)
print(str(bases))

print(''.join(bases))
print(' '.join(bases))
print(', '.join(bases))
```

```python
for b in bases:
    print(b)
```

```python
for b in 'ACGT':
    print(b)
```

```python
print('T' in bases) # Trye
print('U' in bases) # False

print('U' in 'ACGT') # False

print('AC' in 'ACGT') # True
print('AC' in list('ACGT')) # False
```

```python
print(range(10))
print(list(range(10)))
print('*' * 50)

print(list(range(3, 6)))
print(list(range(0, 10, 2)))
print(list(range(0, 10, -1))) # Won't work
print(list(reversed(range(10))))
```

```python
for i in range(5):
    print(i ** 2)
```

```python
some_list = [1, 2, 3]
some_tuple = (1, 2, 3)
print(some_list, some_tuple)
print(some_list == some_tuple) # False
```

```python
some_tuple.append(5)
```

```python
print(some_tuple + (4, 5))
```

```python
a, b, c = some_tuple
print(a, b, c)

A, B, C = some_list
print(A, B, C)
```

```python
a, b = some_tuple
```

```python
_, b, _ = some_tuple
print(b)
```

```python
mono_tuple = (1,)
print(mono_tuple)
a, = mono_tuple
print(a)
(a,) = mono_tuple
print(a)
```

Look out for commas - they are super important!

```python
s = 'The number is: %d.' % 5
print(s)

print('The numbers are: %d, %d, %d.' % (5, 6 , 7))
print('The number is: %d.' % (5,))

print('%s is a string, %d is an integer, %f is a float' % ('blablabla', 6, 6))
print('%d' % 5.5)
```

```python
# It's important to give a tuple, not a list
print('%d and %d' % (1, 2))
print('%d and %d' % [1, 2])
```

```python
print('%d, %d and %d' % tuple(range(3)))
```

```python
print('%d and %d' % tuple(range(3)))
```

```python
print('%s' % 5) # Will work
print('%d' % '5') # Won't work
```

```python
e = 2.71828182846
print('e = %.2f' % e)
```

```python
dictionary = {1: 'one', 2: 'two', 3: 'three'}
print(dictionary)
print(type(dictionary))
print(dictionary[2])
```

```python
print(dictionary[4])
```

```python
print(dictionary.get(4))
print(dictionary.get(4, 'N/A'))
```

```python
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

for key, value in dictionary.items():
    print('%d maps to %s' % (key, value))
```

```python
dictionary[4] = 'four'
print(dictionary)

another_dict = {5: 'five', 6: 'six'}
dictionary.update(another_dict)
print(dictionary)

del dictionary[3]
print(dictionary)
```

```python
a = 55
del a
print(a)
```

```python
print(dict([(1,2), (3,4), (5,6)]))
```

```python
# Example: DNA to RNA

dna_seq = 'ACGTGTCAGTGGGAC'
dna_to_rna = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U'}
rna_letters = []

for nt in dna_seq:
    rna_letters.append(dna_to_rna[nt])
    
rna_seq = ''.join(rna_letters)
print(rna_seq)
```

```python
good_dict = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}
bad_dict = {[0, 0]: 0, [0, 1]: 1, [1, 0]: 2, [1, 1]: 3}
```

```python
my_set = {1, 5, 6, 1, 1, 5}
print(my_set)
print(type(my_set))

print(set([1, 5, 6, 1, 1, 5]))
```

```python
seq = 'ATTTGATTTAGATAGATGATTT'
print('The sequene of length %d has %d unique letters.' % (len(seq), len(set(seq))))
```

```python
very_long_list = list(range(10 ** 6))
very_big_set = set(very_long_list)
number = 512311

print(number in very_long_list) # Slow
print(number in very_big_set) # Fast
```

```python
my_set.add(55)
my_set.add(1)
my_set.add('one')
print(my_set)
```

```python
print({1, 2, 3} | {3, 4, 5})
print({1, 2, 3} & {3, 4, 5})
print({1, 2, 3} - {3, 4, 5})
```
