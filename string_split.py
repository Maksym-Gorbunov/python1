Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 'Here is my split test'
>>> a
'Here is my split test'
>>> type(a)
<class 'str'>
>>> a.split()
['Here', 'is', 'my', 'split', 'test']
>>> a
'Here is my split test'
>>> b = a.split()
>>> a
'Here is my split test'
>>> b
['Here', 'is', 'my', 'split', 'test']
>>> type(b)
<class 'list'>
>>> c = b[3:]
>>> c
['split', 'test']
>>> type(c)
<class 'list'>
>>> a = 'Here-is my split-test'
>>> a
'Here-is my split-test'
>>> b = a.split('-')
>>> b
['Here', 'is my split', 'test']
>>> a
'Here-is my split-test'
>>> a = 'Here-is-my-split test'
>>> a
'Here-is-my-split test'
>>> z= a
>>> z
'Here-is-my-split test'
>>> a,b,c,d = z.split('-')
>>> a
'Here'
>>> b
'is'
>>> c
'my'
>>> d
'split test'
>>> 