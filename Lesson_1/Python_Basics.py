# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Variables & types

var = 10
print(var)
print(var + 1)

# Variable names are case-sensitive!
Var = 11
print(var)
print(Var)

# +
# Valid names
x = 5
some_variable_name55 = 'hello'
NotByTheConventionsButStillValid = 3.14

print(NotByTheConventionsButStillValid + x)
print(x * some_variable_name55)
# -

# Some invalid names
2morrow = 'Wednesday'
variable! = '!'

a, b, c = 1, 2, 3
print(a + b + c)
a = 9
print(a + b + c)

a, b, c = 1, 2, 3, 4
a, b, c = 1, 2

_, x, y, _ = 1, 2, 3, 4
print(x, y)
print(_)

print(x)
print(type(x))

print(type(4), type(3.14), type('some string'))

t = type(x)
print(type(t))

print(type(type(t)))
print(type(t) == type(type(t)))

a = None
print(a)
print(type(a))
print(type(type(a)))

# +
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
# -

condition = (a > b)
print(condition)
print(type(condition))

condition1, condition2 = True, False
print(condition1, condition2)

print((5 > 3) and (2 > 3)) # True and False = False
print((5 > 3) or (2 > 3)) # True or False = True
print(not (5 > 3)) # not True = False
print(not False) # True

print(3 == '3') # False
print(3 != '3') # True
print(3 == 3.0) # True
print(3 == None) # False

print(3 > '3') # Not supported in Python 3, False in Python 2

# +
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

# +
# This is a comment

'''
This is
a long
comment.
'''

"""
Also this.
"""

# +
# Commented out code

# print(5 + 3)
# print(5 - 3)
# -

# # Numbers

x = 2
y = 2.71828182846
print(type(x), type(y))
print(x + y)

print(5 / 2) # Different in Python 2, unless: from __future__ import division
print(5 // 2)
print(4 / 2)

print(5 / 0)

print(5 % 3)

print(5 ** 2712)

print(5.0 ** 2712.0)

print(5.0 ** 123.0)
print(5.0 ** -123.0)
print(4e05)
print(4e-03)
print(1e06 == 10 ** 6)
print(10e06 == 10 ** 6)

print(3.14 ** 2.71)
print((-3.14) ** 2.71) # Results a complex number in Python 3

print(2 * 3 + 4) # 6 + 4 = 10
print(2 * (3 + 4)) # 2 *  7 = 14
print((2 * 3) + 4) # 6 + 4 = 10

x = int('5')
y = float('7.7')
print(x, y, x + y)
print(float('5'))

print(int('7.7'))

print(int(float('7.7')))

print(int(True), int(False), float(True), float(False))

print(int(bool(5)))

# +
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
# -

# # Strings

s1 = 'This is a string'
s2 = "This is also a string"
print(s1)
print(s2)
print(s1 + '. ' + s2 + '.')

# Special chars
print('### Title ###\na:\t5\nb:\t6')

# Escaping
print('### Title ###\\na:\\t5\\nb:\\t6')

print(r'### Title ###\na:\t5\nb:\t6')

print('Don\'t', "Don't")

print(8 * 'cat ')
print('cat ' * 8)

text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(text)
print(len(text))
print(type(len(text)))

print(text[0])
print(text[4])
print(text[-1])
print(text[-4])
print(type(text[0]))

print(text[0:5])
print(text[7:-7])
print(text[7:])
print(text[:-7])
print(text[:3])

print(text[0:10:3])
print(text[:10:3])
print(text[::3])
print(text[::-3])

print(text[::-1])

s1 = str(5)
s2 = str(5.0)
print(s1 + '\n' + s2 + '\n')
print(str(6 > 3))

s = 'text'
print(s)
print(str(s))
print(s == str(s))

print(repr(s))
print(s == repr(s))

s

# +
s += ' 123\t'
print(s)

s *= 3
print(s)
# -

very_long_string = 'This is a very very very long string and there is no problem with that, but we will have to break it ' + \
        'such that it will extend to more than one line'
print(very_long_string)

# +
very_long_string = '''This is another very long string.
This one really goes down to more than one line.
Every new line here really becomes a new line.'''

print(very_long_string)
# -

string = 'An elephant'
substring = 'n el'
contained = substring in string
print(contained)

# # Conditions & loops

# +
a = 6
b = 4

if a > b:
    print('a > b')
else:
    print('a < b')

# +
# Indentation in Python is MUST

if 5 > 3:
print('...')
# -

if 5 > 3:
    print('Ok')
    if 5 > 3:
     print('Not recommended!')

# So are colons
if 5 > 3
    print('Error')

# +
condition1 = a > b
condition2 = a > b + 3
print(condition1, condition2)

if condition1:
    print('a > b')
    
if condition2:
    print('a > b + 3')
    
if condition1 == True:
    print('There is no reason to compare a boolean variable to True.')

# +
if a > b + 3:
    print('a > b + 3')
    
if a > b + 2:
    print('a > b + 2')
    
if a > b + 1:
    print('a > b + 1')
    
if a > b:
    print('a > b')
# -

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

# +
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
# -

for s in 'some string':
    print(s)

# +
dna = 'AAAATCTTGAGATTCGATATGGGA'
A_count = 0

for nt in dna:
    if nt == 'A':
        A_count += 1
        
print(A_count)
# -

print(dna.count('A'))
print(dna.count('AT'))

# +
A_count = 0
i = 0

while i < len(dna):
    
    if dna[i] == 'A':
        A_count += 1
    
    i += 1
    
print(A_count)
print(i, len(dna))

# +
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

# +
# while loops are dangerous (they may result infinite loops)

import time

i = 0

while True:
    i += 1
    print(i)
    # That's actually a very important trick for slowing down infinite loops
    time.sleep(0.5)
# -

for s in 'ABCDEFGHIJK':
    
    if s == 'D':
        continue
    elif s == 'I':
        break
    else: # Not really necessary.
        pass
    
    print(s)

for s1 in 'ABC':
    for s2 in '123':
        
        print(s1 + s2)
        
        if s1 == 'A' and s2 == '2':
            break # Will only affect innermost loop

# # Lists, tuples, dictionaries & sets

l = [1, 2, 3, 'a', 4, 5]
print(l)
print(type(l))
print(len(l))
print(l[1], l[3])

print([1, 2, [1, 2]])
print([1, 2, [1, 2, [1, 2]]])

# +
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
# -

l = [1, 2, 3, 4]
l.append(l)
print(l)
print(l[4])
print(l == l[4])
print(l[4][2])
print(l[4][4][4][4][4][4][4][4][2])

a += 7

# +
a += [11, 12, 13]
print(a)

a += a
print(a)
# -

a = [1, 2, 3]
print(a * 3)
a *= 3
print(a)

print(a[3:8])
print(a[::-1])

# +
bases = list('ACGT')
print(bases)
print(str(bases))

print(''.join(bases))
print(' '.join(bases))
print(', '.join(bases))
# -

for b in bases:
    print(b)

for b in 'ACGT':
    print(b)

# +
print('T' in bases) # Trye
print('U' in bases) # False

print('U' in 'ACGT') # False

print('AC' in 'ACGT') # True
print('AC' in list('ACGT')) # False

# +
print(range(10))
print(list(range(10)))
print('*' * 50)

print(list(range(3, 6)))
print(list(range(0, 10, 2)))
print(list(range(0, 10, -1))) # Won't work
print(list(reversed(range(10))))
# -

for i in range(5):
    print(i ** 2)

some_list = [1, 2, 3]
some_tuple = (1, 2, 3)
print(some_list, some_tuple)
print(some_list == some_tuple) # False

some_tuple.append(5)

print(some_tuple + (4, 5))

# +
a, b, c = some_tuple
print(a, b, c)

A, B, C = some_list
print(A, B, C)
# -

a, b = some_tuple

_, b, _ = some_tuple
print(b)

mono_tuple = (1,)
print(mono_tuple)
a, = mono_tuple
print(a)
(a,) = mono_tuple
print(a)

# Look out for commas - they are super important!

# +
s = 'The number is: %d.' % 5
print(s)

print('The numbers are: %d, %d, %d.' % (5, 6 , 7))
print('The number is: %d.' % (5,))

print('%s is a string, %d is an integer, %f is a float' % ('blablabla', 6, 6))
print('%d' % 5.5)
# -

# It's important to give a tuple, not a list
print('%d and %d' % (1, 2))
print('%d and %d' % [1, 2])

print('%d, %d and %d' % tuple(range(3)))

print('%d and %d' % tuple(range(3)))

print('%s' % 5) # Will work
print('%d' % '5') # Won't work

e = 2.71828182846
print('e = %.2f' % e)

dictionary = {1: 'one', 2: 'two', 3: 'three'}
print(dictionary)
print(type(dictionary))
print(dictionary[2])

print(dictionary[4])

print(dictionary.get(4))
print(dictionary.get(4, 'N/A'))

# +
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

for key, value in dictionary.items():
    print('%d maps to %s' % (key, value))

# +
dictionary[4] = 'four'
print(dictionary)

another_dict = {5: 'five', 6: 'six'}
dictionary.update(another_dict)
print(dictionary)

del dictionary[3]
print(dictionary)
# -

a = 55
del a
print(a)

print(dict([(1,2), (3,4), (5,6)]))

# +
# Example: DNA to RNA

dna_seq = 'ACGTGTCAGTGGGAC'
dna_to_rna = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'U'}
rna_letters = []

for nt in dna_seq:
    rna_letters.append(dna_to_rna[nt])
    
rna_seq = ''.join(rna_letters)
print(rna_seq)
# -

good_dict = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}
bad_dict = {[0, 0]: 0, [0, 1]: 1, [1, 0]: 2, [1, 1]: 3}

# +
my_set = {1, 5, 6, 1, 1, 5}
print(my_set)
print(type(my_set))

print(set([1, 5, 6, 1, 1, 5]))
# -

seq = 'ATTTGATTTAGATAGATGATTT'
print('The sequene of length %d has %d unique letters.' % (len(seq), len(set(seq))))

# +
very_long_list = list(range(10 ** 6))
very_big_set = set(very_long_list)
number = 512311

print(number in very_long_list) # Slow
print(number in very_big_set) # Fast
# -

my_set.add(55)
my_set.add(1)
my_set.add('one')
print(my_set)

print({1, 2, 3} | {3, 4, 5})
print({1, 2, 3} & {3, 4, 5})
print({1, 2, 3} - {3, 4, 5})
