Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.



1int=10
SyntaxError: invalid decimal literal




_a_=10


typr(_a_)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    typr(_a_)
NameError: name 'typr' is not defined. Did you mean: 'type'?





type(_a_)
<class 'int'>


type(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined








if=1
SyntaxError: invalid syntax




while=1
SyntaxError: invalid syntax


$count=1
SyntaxError: invalid syntax





import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']







help("list")
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None



=============================================================== RESTART: D:\Goli\p_time\p_time\12_03_2024_ide_keywords.py ==============================================================
Printing possible keywords in python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
Total keyword count is : 35
Enter a word to search its a python keywordpass
entered word is keyword
Enter a word to search its a python keyword
Traceback (most recent call last):
  File "D:\Goli\p_time\p_time\12_03_2024_ide_keywords.py", line 13, in <module>
    key_search = str(input('Enter a word to search its a python keyword'))
KeyboardInterrupt








a=int()

trye(a)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    trye(a)
NameError: name 'trye' is not defined. Did you mean: 'True'?
type(a)
<class 'int'>



a=10-
SyntaxError: invalid syntax
a=10
a=20
a
20


type(a)
<class 'int'>



a=1.2
type(a)
<class 'float'>



a
1.2


id(a)
2271737949456



print(a)
1.2



type(a)
<class 'float'>
id(a)
2271737949456

print(a)
1.2










a=0b
SyntaxError: invalid binary literal
a=0b111
type(a)
<class 'int'>
print(a)
7

id(a)
2271698354608



a=0B1111
a
15





b=0b000
c=0b000
print(b,c)
0 0




b=0B000
c=0b000
print(b,c)
0 0


b=0B001
c=0b001
print(b,c)
1 1


id(c)
2271698354416
id(b)
2271698354416
id(c)=id(b)
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
id(c)==id(b):
    
SyntaxError: invalid syntax




is id(c)==id(b)
SyntaxError: invalid syntax

a==b
False
b==c
True









clear
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    clear
NameError: name 'clear' is not defined





cls
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    cls
NameError: name 'cls' is not defined













a=0o111
b=0O111
a==b
True

print(a,b)
73 73



id(a)
2271698356720
id(b)
2271698356720










a=0x1goli
SyntaxError: invalid hexadecimal literal
a=0xa1
a
161




b=0Xa1
b
161


id(a,b)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    id(a,b)
TypeError: id() takes exactly one argument (2 given)
id9a)
SyntaxError: unmatched ')'
id(a)
2271698359536
id(b)
2271698359536
a=0xabcdef
a
11259375










bin(10)
'0b1010'




bin(0b1010)
'0b1010'



bin(0x1a)
'0b11010'




hex(0b11010)
'0x1a'


hex(10)
'0xa'
oct(10)
'0o12'
bin(10)
'0b1010'



dec(0b1010)
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    dec(0b1010)
NameError: name 'dec' is not defined








int(0b1010,2)
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    int(0b1010,2)
TypeError: int() can't convert non-string with explicit base

    


int('0b1010',2)
10
int('0xa',16)
10


int('0o12',7)
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    int('0o12',7)
ValueError: invalid literal for int() with base 7: '0o12'
int('0o12',8)
10



























cls
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
import os
cls
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
os.system(cls)
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    os.system(cls)
NameError: name 'cls' is not defined


os.system.cls
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    os.system.cls
AttributeError: 'builtin_function_or_method' object has no attribute 'cls'




os.system.cls()
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    os.system.cls()
AttributeError: 'builtin_function_or_method' object has no attribute 'cls'

os.system('cls' if os.name == 'nt' else 'clear')
0




0
0





a=1.2
type(a)
<class 'float'>







a=2
a=1.e
SyntaxError: invalid decimal literal
SyntaxError: invalid decimal literal
SyntaxError: invalid syntax





a=1.1e
SyntaxError: invalid decimal literal
a=1e3
a
1000.0




print(a)
1000.0



type(a)
<class 'float'>



a=0b01.1
SyntaxError: invalid syntax




b=0O2.5
SyntaxError: invalid syntax








a=b+cj
Traceback (most recent call last):
  File "<pyshell#346>", line 1, in <module>
    a=b+cj
NameError: name 'cj' is not defined. Did you mean: 'c'?




a=10+2j
type(a)
<class 'complex'>



b=20-1j

type(b)
<class 'complex'>
c=b-a
c
(10-3j)
c.real
10.0
c.imag
-3.0



a='goli
SyntaxError: unterminated string literal (detected at line 1)
a='goli'
b="goli"
a
'goli'
b
'goli'
a==b
True


id(a)
2271739917808
id(b)
2271739917808



a="Goli
SyntaxError: unterminated string literal (detected at line 1)
a='''goli
narasimha
is my name'''
a
'goli\nnarasimha\nis my name'

==================================================================================== RESTART: Shell ====================================================================================































a='narasimha Goli'
type(a)
<class 'str'>





len(a)
14




a[0]
'n'



for character in a:
    print(character)

    
n
a
r
a
s
i
m
h
a
 
G
o
l
i
for character in a:
    print(character,sep='   ')

    
n
a
r
a
s
i
m
h
a
 
G
o
l
i
a[1:6:1]
'arasi'
help('enumerate')
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |  
 |  Return an enumerate object.
 |  
 |    iterable
 |      an object supporting iteration
 |  
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |  
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.






a
'narasimha Goli'




for index,chat in enumerate(a)
SyntaxError: expected ':'

for index,char in enumerate(a):
    print(char,'at localtion of:', index)

    
n at localtion of: 0
a at localtion of: 1
r at localtion of: 2
a at localtion of: 3
s at localtion of: 4
i at localtion of: 5
m at localtion of: 6
h at localtion of: 7
a at localtion of: 8
  at localtion of: 9
G at localtion of: 10
o at localtion of: 11
l at localtion of: 12
i at localtion of: 13
i at localtion of: 13
SyntaxError: invalid syntax





a
'narasimha Goli'




a[::13]
'ni'
a[0::]
'narasimha Goli'
a[::50]
'n'
a[1,4]
Traceback (most recent call last):
  File "<pyshell#448>", line 1, in <module>
    a[1,4]
TypeError: string indices must be integers
TypeError: string indices must be integersa
SyntaxError: invalid syntax




a[1:4]
'ara'
a[1:4:4]
'a'



len(a0


    )
Traceback (most recent call last):
  File "<pyshell#462>", line 1, in <module>
    len(a0
NameError: name 'a0' is not defined. Did you mean: 'a'?
len(a)
        
14




for index,char in enumerate(a):
    print(char,'at localtion of:', index)

        
n at localtion of: 0
a at localtion of: 1
r at localtion of: 2
a at localtion of: 3
s at localtion of: 4
i at localtion of: 5
m at localtion of: 6
h at localtion of: 7
a at localtion of: 8
  at localtion of: 9
G at localtion of: 10
o at localtion of: 11
l at localtion of: 12
i at localtion of: 13


a.capitalize()
        
'Narasimha goli'
a
        
'narasimha Goli'
a.count(a)
        
1
1
        
1


a.count('a')
        
3
a.count('i')
        
2
a.islower()
        
False



a
        
'narasimha Goli'



a.isupper()
        
False

a[0:6:1]
        
'narasi'


a[::2]
        
'nrsmaGl'

a[2::2]
        
'rsmaGl'
a[:-1]
        
'narasimha Gol'
a[:-1]
        
'narasimha Gol'
a[::]
        
'narasimha Goli'




help('str')
        
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |      
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |      
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |      
 |        sep
 |          The separator used to split the string.
 |      
 |          When set to None (the default value), will split on any whitespace
 |          character (including \\n \\r \\t \\f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits (starting from the left).
 |          -1 (the default value) means no limit.
 |      
 |      Splitting starts at the end of the string and works to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |      
 |        sep
 |          The separator used to split the string.
 |      
 |          When set to None (the default value), will split on any whitespace
 |          character (including \\n \\r \\t \\f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits (starting from the left).
 |          -1 (the default value) means no limit.
 |      
 |      Note, str.split() is mainly useful for data that has been intentionally
 |      delimited.  With natural text that includes punctuation, consider using
 |      the regular expression module.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(...)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

|      case.
SyntaxError: invalid syntax
__sizeof__(a)
Traceback (most recent call last):
  File "<pyshell#503>", line 1, in <module>
    __sizeof__(a)
NameError: name '__sizeof__' is not defined
a.__sizeof__()
63

a.__len__()
14




len(a)
14

help('str')
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |      
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |      
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |      
 |        sep
 |          The separator used to split the string.
 |      
 |          When set to None (the default value), will split on any whitespace
 |          character (including \\n \\r \\t \\f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits (starting from the left).
 |          -1 (the default value) means no limit.
 |      
 |      Splitting starts at the end of the string and works to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |      
 |        sep
 |          The separator used to split the string.
 |      
 |          When set to None (the default value), will split on any whitespace
 |          character (including \\n \\r \\t \\f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits (starting from the left).
 |          -1 (the default value) means no limit.
 |      
 |      Note, str.split() is mainly useful for data that has been intentionally
 |      delimited.  With natural text that includes punctuation, consider using
 |      the regular expression module.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(...)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.



|  __contains__(self, key, /)
|      Return key in self.
SyntaxError: invalid syntax



a.__contains__('Goli')
True


a.__contains__('goli')
False

a.__contains__('a')
True
a.__contains__('N')
False
a
'narasimha Goli'






a[10]
'G'
a[10]=g
Traceback (most recent call last):
  File "<pyshell#533>", line 1, in <module>
    a[10]=g
NameError: name 'g' is not defined
a[10]='g'
Traceback (most recent call last):
  File "<pyshell#534>", line 1, in <module>
    a[10]='g'
TypeError: 'str' object does not support item assignment




f=0B1111
f
15



int(f)
15
int(f,2)
Traceback (most recent call last):
  File "<pyshell#545>", line 1, in <module>
    int(f,2)
TypeError: int() can't convert non-string with explicit base



int('0B1111',2)
15






int(14.3)
14



int('Goli')
Traceback (most recent call last):
  File "<pyshell#560>", line 1, in <module>
    int('Goli')
ValueError: invalid literal for int() with base 10: 'Goli'



int(10+3j)
Traceback (most recent call last):
  File "<pyshell#564>", line 1, in <module>
    int(10+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'





int(true)
        
Traceback (most recent call last):
  File "<pyshell#569>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
        
1


int(None)
        
Traceback (most recent call last):
  File "<pyshell#573>", line 1, in <module>
    int(None)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'




int(False)
        
0



int(if)
        
SyntaxError: invalid syntax



int('10.4')
        
Traceback (most recent call last):
  File "<pyshell#585>", line 1, in <module>
    int('10.4')
ValueError: invalid literal for int() with base 10: '10.4'



int(10.4)
        
10


int(0b111)
        
7
int(0b111,2)
        
Traceback (most recent call last):
  File "<pyshell#593>", line 1, in <module>
    int(0b111,2)
TypeError: int() can't convert non-string with explicit base
int('0b111',2)
        
7



float('0b111',2)
        
Traceback (most recent call last):
  File "<pyshell#598>", line 1, in <module>
    float('0b111',2)
TypeError: float expected at most 1 argument, got 2



float('0b111')
        
Traceback (most recent call last):
  File "<pyshell#602>", line 1, in <module>
    float('0b111')
ValueError: could not convert string to float: '0b111'




float("ten")
        
Traceback (most recent call last):
  File "<pyshell#607>", line 1, in <module>
    float("ten")
ValueError: could not convert string to float: 'ten'



complex(5)
        
(5+0j)
complex(10.5)
        
(10.5+0j)
complex(10,5)
        
(10+5j)
complex("0b1111")
        
Traceback (most recent call last):
  File "<pyshell#614>", line 1, in <module>
    complex("0b1111")
ValueError: complex() arg is a malformed string
complex(0b1111)
        
(15+0j)
bool(10)
        
True



True+True
        
2


True+False
        
1
True+False+None
        
Traceback (most recent call last):
  File "<pyshell#624>", line 1, in <module>
    True+False+None
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

bool(false)
        
Traceback (most recent call last):
  File "<pyshell#626>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined. Did you mean: 'False'?


bool('false')
        
True




str(10)
        
'10'

a='10'
        
type(a)
        
<class 'str'>



a=10
        
type(a)
        
<class 'int'>








a=10
        
b=10
        
id(a)
        
2726892864016
id(b)
        
2726892864016
a==b
        
True
a is b
        
True
a='Goli'
        
b='Goli'
        
a is b
        
True

id(a)
        
2726933938800
id(b)
        
2726933938800








x=10+5j
        
y=10+5j
        
x is y
        
False


2726933938800
        
2726933938800







id(x)
        
2726932459728
id(y)
        
2726932460304




f1=1.3
        
f2=1.3
        
type(f1)
        
<class 'float'>


f1 is f2
        
False

f1=1.3

f2=1.3

type(f1)

<class 'float'>


f1 is f2

SyntaxError: multiple statements found while compiling a single statement
id(f1)
        
2726932461584
id(f2)
        
2726903198224



b1 =True
        
b2=True
        
b1 is b2
        
True



id(b1)
        
140717938953064
id(b2)
        
140717938953064



s1='Goli'
        
s2='Goli'
        
type(s1)
        
<class 'str'>
type(s2)
        
<class 'str'>


id(s1)
        
2726933938800
id(s2)
        
2726933938800


s1 is s2
        
True








a=b'i am narasimha goli'
        
type(a)
        
<class 'bytes'>



a
        
b'i am narasimha goli'
print(a)
        
b'i am narasimha goli'


a[0]
        
105
for index,char in a :
        print(index,char)

        
Traceback (most recent call last):
  File "<pyshell#742>", line 1, in <module>
    for index,char in a :
TypeError: cannot unpack non-iterable int object
for index,char in enumerate(a) :
        print(index,char)

        
0 105
1 32
2 97
3 109
4 32
5 110
6 97
7 114
8 97
9 115
10 105
11 109
12 104
13 97
14 32
15 103
16 111
17 108
18 105
a
        
b'i am narasimha goli'
x=[10,11,12,13,14,15]
        
type(x)
        
<class 'list'>


b=bytes(x)
        
b
        
b'\n\x0b\x0c\r\x0e\x0f'



type(b)
        
<class 'bytes'>


print(b)
        
b'\n\x0b\x0c\r\x0e\x0f'


b[0]
        
10


b[1]
        
11
b[-1]
        
15











s1="Hi my name is narasimha goli"
        


s1
        
'Hi my name is narasimha goli'


type(s1)
        
<class 'str'>




byte_str=s1.encode('utf-8')
        


type(byte_str)
        
<class 'bytes'>



byte_str
        
b'Hi my name is narasimha goli'
string_back=byte_str.decode('utf-8')
        

string_back
        
'Hi my name is narasimha goli'
type(string_back)
        
<class 'str'>





x
        
[10, 11, 12, 13, 14, 15]
b
        
b'\n\x0b\x0c\r\x0e\x0f'




b[0]
        
10



b[0]=100
        
Traceback (most recent call last):
  File "<pyshell#812>", line 1, in <module>
    b[0]=100
TypeError: 'bytes' object does not support item assignment

c=b'10
        
SyntaxError: unterminated string literal (detected at line 1)
c=b'10'
        
type(c)
        
<class 'bytes'>



print(c)
        
b'10'


x
        
[10, 11, 12, 13, 14, 15]
b
        
b'\n\x0b\x0c\r\x0e\x0f'





b=bytearray(x)
        
type(x)
        
<class 'list'>
type(b)
        
<class 'bytearray'>



b[0]
        
10
b[0]=16
        


b
        
bytearray(b'\x10\x0b\x0c\r\x0e\x0f')
b[0]
        
16






l1=[10,10.5,'goli','True',10+3j]
        
11
        
11
l1
        
[10, 10.5, 'goli', 'True', (10+3j)]



tyep(l1)
        
Traceback (most recent call last):
  File "<pyshell#851>", line 1, in <module>
    tyep(l1)
NameError: name 'tyep' is not defined
type(l1)
        
<class 'list'>


l1[0]
        
10


for index,char in enumerate(l1):
        print('Content at location:',index 'is:',char,'and its data type is:'type(char))
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
for index,char in enumerate(l1):
        print('Content at location:',index 'is:',char,'and its data type is:',type(char))
        
SyntaxError: invalid syntax

for index,char in enumerate(l1):
        print('Content at location:',index,'is:',char,'and its data type is:',type(char))

        
Content at location: 0 is: 10 and its data type is: <class 'int'>
Content at location: 1 is: 10.5 and its data type is: <class 'float'>
Content at location: 2 is: goli and its data type is: <class 'str'>
Content at location: 3 is: True and its data type is: <class 'str'>
Content at location: 4 is: (10+3j) and its data type is: <class 'complex'>
l1
        
[10, 10.5, 'goli', 'True', (10+3j)]
l1[3]=True
        
type(l1[3])
        
<class 'bool'>

for index,char in enumerate(l1):
        print('Content at location:',index,'is:',char,'and its data type is:',type(char))

        
Content at location: 0 is: 10 and its data type is: <class 'int'>
Content at location: 1 is: 10.5 and its data type is: <class 'float'>
Content at location: 2 is: goli and its data type is: <class 'str'>
Content at location: 3 is: True and its data type is: <class 'bool'>
Content at location: 4 is: (10+3j) and its data type is: <class 'complex'>



l1
        
[10, 10.5, 'goli', True, (10+3j)]


t1=tuple(l1)
        
t1
        
(10, 10.5, 'goli', True, (10+3j))
type(t1)
        
<class 'tuple'>


print(t1)
        
(10, 10.5, 'goli', True, (10+3j))



t1[6]='Goli
        
SyntaxError: unterminated string literal (detected at line 1)
t1[6]='Goli'
        
Traceback (most recent call last):
  File "<pyshell#884>", line 1, in <module>
    t1[6]='Goli'
TypeError: 'tuple' object does not support item assignment




t1
        
(10, 10.5, 'goli', True, (10+3j))





t1[0]
        
10



for index,char in enumerate(t1):
        print('Content at location:',index,'is:',char,'and its data type is:',type(char))

        
Content at location: 0 is: 10 and its data type is: <class 'int'>
Content at location: 1 is: 10.5 and its data type is: <class 'float'>
Content at location: 2 is: goli and its data type is: <class 'str'>
Content at location: 3 is: True and its data type is: <class 'bool'>
Content at location: 4 is: (10+3j) and its data type is: <class 'complex'>



l1
        
[10, 10.5, 'goli', True, (10+3j)]




l1.append(False)
        
l1
        
[10, 10.5, 'goli', True, (10+3j), False]



t1.count()
        
Traceback (most recent call last):
  File "<pyshell#910>", line 1, in <module>
    t1.count()
TypeError: tuple.count() takes exactly one argument (0 given)


t1.count('goli')
        
1


t1.index
        
<built-in method index of tuple object at 0x0000027AE9E3FD80>
t1.index()
        
Traceback (most recent call last):
  File "<pyshell#917>", line 1, in <module>
    t1.index()
TypeError: index expected at least 1 argument, got 0




help(tuple.index)
        
Help on method_descriptor:

index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    
    Raises ValueError if the value is not present.

index(t1,'goli')
        
Traceback (most recent call last):
  File "<pyshell#922>", line 1, in <module>
    index(t1,'goli')
TypeError: 'int' object is not callable






l1
        
[10, 10.5, 'goli', True, (10+3j), False]
l1[0]
        
10



l1[::]
        
[10, 10.5, 'goli', True, (10+3j), False]
l1[1:4:2]
        
[10.5, True]


l1[1:-1:1]
        
[10.5, 'goli', True, (10+3j)]


t1
        
(10, 10.5, 'goli', True, (10+3j))



t1[1:9]
        
(10.5, 'goli', True, (10+3j))


t1[2:5:2]
        
('goli', (10+3j))




help('list')
        
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

The argument must be an iterable if specified.
SyntaxError: expected 'else' after 'if' expression

l1
[10, 10.5, 'goli', True, (10+3j), False]
l1.reverse()

l1
[False, (10+3j), True, 'goli', 10.5, 10]
l1.count('goli')
1


l1.index()
Traceback (most recent call last):
  File "<pyshell#963>", line 1, in <module>
    l1.index()
TypeError: index expected at least 1 argument, got 0
File "<pyshell#963>", line 1, in <module>l1.
SyntaxError: invalid syntax
File "<pyshell#963>", line 1, in <module>l1.

l1.index('goli')
3


l1
[False, (10+3j), True, 'goli', 10.5, 10]


l1.__contains__('goli')
True





l1.pop()
10
l1
[False, (10+3j), True, 'goli', 10.5]
l1.reverse()
l1
[10.5, 'goli', True, (10+3j), False]
l1.insert(5,10)
l1
[10.5, 'goli', True, (10+3j), False, 10]


l1.append(20)
l1
[10.5, 'goli', True, (10+3j), False, 10, 20]




l1.sort()
Traceback (most recent call last):
  File "<pyshell#993>", line 1, in <module>
    l1.sort()
TypeError: '<' not supported between instances of 'str' and 'float'


l2=[]
l2=range(1,10,2)
l2
range(1, 10, 2)


print(l2)
range(1, 10, 2)
range(1, 10, 2)
range(1, 10, 2)

l2=list(range(1,10,2))
l2
[1, 3, 5, 7, 9]
l2.sort()
l2
[1, 3, 5, 7, 9]
l2.reverse()
l2
[9, 7, 5, 3, 1]

l2.sort()

l2
[1, 3, 5, 7, 9]
l3=l2.reserve()
Traceback (most recent call last):
  File "<pyshell#1012>", line 1, in <module>
    l3=l2.reserve()
AttributeError: 'list' object has no attribute 'reserve'. Did you mean: 'reverse'?
l2
[1, 3, 5, 7, 9]



l2.reverse()
l2
[9, 7, 5, 3, 1]
l3=l2
l3
[9, 7, 5, 3, 1]
l2
[9, 7, 5, 3, 1]
l2.reverse()


l2
[1, 3, 5, 7, 9]
l



l2
[1, 3, 5, 7, 9]
l
l3
[1, 3, 5, 7, 9]
l2.reverse()

l2
[9, 7, 5, 3, 1]
l3
[9, 7, 5, 3, 1]











l1=list(range(1,10,2))
l1
[1, 3, 5, 7, 9]
l2=l1.reverse()
l2


l2=l1
l1
[9, 7, 5, 3, 1]
l2
[9, 7, 5, 3, 1]
l2.reserve()
Traceback (most recent call last):
  File "<pyshell#1053>", line 1, in <module>
    l2.reserve()
AttributeError: 'list' object has no attribute 'reserve'. Did you mean: 'reverse'?
l2.reverse()

l1
[1, 3, 5, 7, 9]
l2
[1, 3, 5, 7, 9]






l2 = l1[::-1]
l2
[9, 7, 5, 3, 1]





t1
(10, 10.5, 'goli', True, (10+3j))
t1.reverse()
Traceback (most recent call last):
  File "<pyshell#1068>", line 1, in <module>
    t1.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'



r=range(1,10)
type(r)
<class 'range'>





r
range(1, 10)


print(r)
range(1, 10)



r[0]
1
r[1]
2
r[]
SyntaxError: invalid syntax
r[::]
range(1, 10)
r[:]
range(1, 10)



range[::-]
SyntaxError: invalid syntax



for i in r:
    print(i)

    
1
2
3
4
5
6
7
8
9
r[0]=100
Traceback (most recent call last):
  File "<pyshell#1098>", line 1, in <module>
    r[0]=100
TypeError: 'range' object does not support item assignment



b1=b'257'
b1
b'257'
type(b1)
<class 'bytes'>




l1
[1, 3, 5, 7, 9]
b1=bytes(l1)
b1
b'\x01\x03\x05\x07\t'
b1[0]
1







l1
[1, 3, 5, 7, 9]
l1.append(9)
l1
[1, 3, 5, 7, 9, 9]




s1=set(l1)
s1
{1, 3, 5, 7, 9}


l1
[1, 3, 5, 7, 9, 9]



t1
(10, 10.5, 'goli', True, (10+3j))



s2=set(t1)
s2
{True, 'goli', 10, 10.5, (10+3j)}

l1
[1, 3, 5, 7, 9, 9]

type(s1)
<class 'set'>


type(s2)
<class 'set'>


s2
{True, 'goli', 10, 10.5, (10+3j)}
s2.add('goli')
s2
{True, 'goli', 10, 10.5, (10+3j)}
s2.remove('goli')
s2
{True, 10, 10.5, (10+3j)}





s2.add('goli')
s2
{True, 'goli', 10, 10.5, (10+3j)}


s1
{1, 3, 5, 7, 9}
s2
{True, 'goli', 10, 10.5, (10+3j)}


s1[0]
Traceback (most recent call last):
  File "<pyshell#1166>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable


s1
{1, 3, 5, 7, 9}



fs1=frozenset(s1)


fs1
frozenset({1, 3, 5, 7, 9})
({1, 3, 5, 7, 9})
{1, 3, 5, 7, 9}





help('dict')
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      
 |      If the key is not found, return the default if given; otherwise,
 |      raise a KeyError.
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None






d1=dict{}
SyntaxError: invalid syntax

d1=
SyntaxError: invalid syntax

d1=dict()



type(d1)
<class 'dict'>



d1['goli']=100
d1
{'goli': 100}


d1['goli']=200


d1
{'goli': 200}


d1['kiran']=300
d1['avadh']=400
d1
{'goli': 200, 'kiran': 300, 'avadh': 400}






d1
{'goli': 200, 'kiran': 300, 'avadh': 400}
enumerate(d1)
<enumerate object at 0x0000027AE9EE8740>




for key,value in enumerate(d1):
    print(key,':',value)

    
0 : goli
1 : kiran
2 : avadh





d1
{'goli': 200, 'kiran': 300, 'avadh': 400}
d1.keys
<built-in method keys of dict object at 0x0000027AE9ED3F40>
print(d1.keys)
<built-in method keys of dict object at 0x0000027AE9ED3F40>



for key in d1.keys:
    print(key)

    
Traceback (most recent call last):
  File "<pyshell#1239>", line 1, in <module>
    for key in d1.keys:
TypeError: 'builtin_function_or_method' object is not iterable
for key in d1.keys():
    print(key)

    
goli
kiran
avadh


help('dict')
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      
 |      If the key is not found, return the default if given; otherwise,
 |      raise a KeyError.
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

object providing a view on D's values
SyntaxError: unterminated string literal (detected at line 1)
object providing a view on D's values




d1
{'goli': 200, 'kiran': 300, 'avadh': 400}



d1.items()
dict_items([('goli', 200), ('kiran', 300), ('avadh', 400)])







for key,value in d1.items():
    print( 'Key:',Key,'Value:',value)

    
Traceback (most recent call last):
  File "<pyshell#1265>", line 2, in <module>
    print( 'Key:',Key,'Value:',value)
NameError: name 'Key' is not defined. Did you mean: 'key'?
for key,value in d1.items():
    print( 'Key:',key,'Value:',value)

    
Key: goli Value: 200
Key: kiran Value: 300
Key: avadh Value: 400
for key,value in d1.items():
    print( Key,value)

    
Traceback (most recent call last):
  File "<pyshell#1269>", line 2, in <module>
    print( Key,value)
NameError: name 'Key' is not defined. Did you mean: 'key'?
for key,value in d1.items():
    print(key,value)

    
goli 200
kiran 300
avadh 400
od=ordereddict()
Traceback (most recent call last):
  File "<pyshell#1272>", line 1, in <module>
    od=ordereddict()
NameError: name 'ordereddict' is not defined


import collections
ordereddict1=OrderedDict()
Traceback (most recent call last):
  File "<pyshell#1276>", line 1, in <module>
    ordereddict1=OrderedDict()
NameError: name 'OrderedDict' is not defined


from collections import orderedDict
Traceback (most recent call last):
  File "<pyshell#1278>", line 1, in <module>
    from collections import orderedDict
ImportError: cannot import name 'orderedDict' from 'collections' (C:\Users\avadh\AppData\Local\Programs\Python\Python310\lib\collections\__init__.py)
from collections import OrderedDict
my_ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(my_ordered_dict)
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
type(my_ordered_dict)
<class 'collections.OrderedDict'>


my_ordered_dict[0]
Traceback (most recent call last):
  File "<pyshell#1285>", line 1, in <module>
    my_ordered_dict[0]
KeyError: 0


for key,value in my_ordered_dict.items():
    print(key,value)

    
a 1
b 2
c 3


OrderedDict([('a', 1), ('b', 2), ('c', 3)])
OrderedDict([('a', 1), ('b', 2), ('c', 3)])













a=10
b=2



a=b
a
2
b
2




a=10
b=2
a+b
12


a-b
8
a/b
5.0
a%b
0
a*b
20
a//b
5
a**b
100
a**b
100
SyntaxError: multiple statements found while compiling a single statement
a**b
100








a=goli
Traceback (most recent call last):
  File "<pyshell#1334>", line 1, in <module>
    a=goli
NameError: name 'goli' is not defined
a='goli'
b='narasimha'
a
'goli'
b
'narasimha'
c=a+b
c
'golinarasimha'



d=3
a*d
'goligoligoli'


a+d
Traceback (most recent call last):
  File "<pyshell#1348>", line 1, in <module>
    a+d
TypeError: can only concatenate str (not "int") to str



a
'goli'
b
'narasimha'
a=19
b=2



a<b
False
a>b
True
a<=b
False
a>=b
True
10==20
False
10!=20
True





10 and 20
20


0 and 20
0


10 or 20
10


not 10
False


not ""
True




4&5
4



print(4&5)
4


4|5
5

a=10
b=2-
SyntaxError: invalid syntax






















a=10
b=20
c=30


min=a if a<b else b
min
10



min=a if a<b and if a<c else b
SyntaxError: expected 'else' after 'if' expression
min=a if a<b and a<c else b
min
10


a=30
b=20
c=10

min=a if a<b and a<c else b
min
20
a=30
b=20
c=10

min=a if a<b and a<c else b
SyntaxError: multiple statements found while compiling a single statement
a=30
b=20
c=10

min=a if a<b and a<c else b







a
30
b
20
c
10




min=a if a<b else ( b if b<c else c)
min
10








min = a if a<b and a<c else b if b<c else c
min
10
min = a if a<b else (b if b<c else c)
min
10



a=10
b=20
c=30
min = a if a<b and a<c else b if b<c else c
min
10


min="'
SyntaxError: unterminated string literal (detected at line 1)
min=''
min
''
min = a if a<b and a<c else b if b<c else c
min
10
min=''

min = a if a<b else (b if b<c else c)
min
10



a
10
a,b,c
(10, 20, 30)
a,b,c=30,20,10
min = a if a<b and a<c else b if b<c else c
min1 = a if a<b else (b if b<c else c)
min
10
min1
10





a,b,c=10,20,30



max = a if a>b else (b if b>c else c)
max
30



max1 = a if a>b and a>c else b if b>c else c
max1
30
max
30
max1
30



max is max1
True



id(max)
2726892864656
id(max1)
2726892864656


max is not max1
False



help('modules')

Please wait a moment while I gather a list of all available modules...

__future__          ast                 history             sched
__main__            asynchat            hmac                scrolledlist
_abc                asyncio             html                search
_aix_support        asyncore            http                searchbase
_ast                atexit              hyperparser         searchengine
_asyncio            audioop             idle                secrets
_bisect             autocomplete        idle_test           select
_blake2             autocomplete_w      idlelib             selectors
_bootsubprocess     autoexpand          idna                setuptools
_bz2                base64              imaplib             shelve
_codecs             bdb                 imghdr              shlex
_codecs_cn          binascii            imp                 shutil
_codecs_hk          binhex              importlib           sidebar
_codecs_iso2022     bisect              inspect             signal
_codecs_jp          browser             io                  site
_codecs_kr          builtins            iomenu              six
_codecs_tw          bz2                 ipaddress           smtpd
_collections        cProfile            itertools           smtplib
_collections_abc    calendar            json                sndhdr
_compat_pickle      calltip             keyword             socket
_compression        calltip_w           lib2to3             socketserver
_contextvars        certifi             linecache           sqlite3
_csv                cgi                 locale              squeezer
_ctypes             cgitb               logging             sre_compile
_ctypes_test        charset_normalizer  lzma                sre_constants
_datetime           chunk               macosx              sre_parse
_decimal            cmath               mailbox             ssl
_distutils_hack     cmd                 mailcap             stackviewer
_elementtree        code                mainmenu            stat
_functools          codecontext         marshal             statistics
_hashlib            codecs              math                statusbar
_heapq              codeop              mimetypes           string
_imp                collections         mmap                stringprep
_io                 colorizer           modulefinder        struct
_json               colorsys            msilib              subprocess
_locale             compileall          msvcrt              sunau
_lsprof             concurrent          multicall           symtable
_lzma               config              multiprocessing     sys
_markupbase         config_key          netrc               sysconfig
_md5                configdialog        nntplib             tabnanny
_msi                configparser        nt                  tarfile
_multibytecodec     contextlib          ntpath              telnetlib
_multiprocessing    contextvars         nturl2path          tempfile
_opcode             copy                numbers             test
_operator           copyreg             opcode              textview
_osx_support        crypt               operator            textwrap
_overlapped         csv                 optparse            this
_pickle             ctypes              os                  threading
_py_abc             curses              outwin              time
_pydecimal          dataclasses         parenmatch          timeit
_pyio               datetime            pathbrowser         tkinter
_queue              dbm                 pathlib             token
_random             debugger            pdb                 tokenize
_sha1               debugger_r          percolator          tooltip
_sha256             debugobj            pickle              trace
_sha3               debugobj_r          pickletools         traceback
_sha512             decimal             pip                 tracemalloc
_signal             delegator           pipes               tree
_sitebuiltins       difflib             pkg_resources       tty
_socket             dis                 pkgutil             turtle
_sqlite3            distutils           platform            turtledemo
_sre                doctest             plistlib            types
_ssl                dynoption           poplib              typing
_stat               editor              posixpath           undo
_statistics         email               pprint              unicodedata
_string             encodings           profile             unittest
_strptime           ensurepip           pstats              urllib
_struct             enum                pty                 urllib3
_symtable           errno               pyVim               util
_testbuffer         faulthandler        pyVmomi             uu
_testcapi           filecmp             py_compile          uuid
_testconsole        fileinput           pyclbr              venv
_testimportmultiple filelist            pydoc               warnings
_testinternalcapi   fnmatch             pydoc_data          wave
_testmultiphase     format              pyexpat             weakref
_thread             fractions           pyparse             webbrowser
_threading_local    ftplib              pyshell             window
_tkinter            functools           query               winreg
_tracemalloc        gc                  queue               winsound
_uuid               genericpath         quopri              wsgiref
_warnings           getopt              random              xdrlib
_weakref            getpass             re                  xml
_weakrefset         gettext             redirector          xmlrpc
_winapi             glob                replace             xxsubtype
_xxsubinterpreters  graphlib            reprlib             zipapp
_zoneinfo           grep                requests            zipfile
abc                 gzip                rlcompleter         zipimport
aifc                hashlib             rpc                 zlib
antigravity         heapq               run                 zoneinfo
argparse            help                runpy               zoomheight
array               help_about          runscript           zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

netrc
Traceback (most recent call last):
  File "<pyshell#1510>", line 1, in <module>
    netrc
NameError: name 'netrc' is not defined





help('math')
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        
        The result is between 0 and pi.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(*integers)
        Greatest Common Divisor.
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    lcm(*integers)
        Least Common Multiple.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    nextafter(x, y, /)
        Return the next floating-point value after x towards y.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.
    
    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


acosh(x, /)
    Return the inverse hyperbolic cosine of x.

asin(x, /)
    Return the arc sine (measured in radians) of x.

    The result is between -pi/2 and pi/2.

asinh(x, /)
    Return the inverse hyperbolic sine of x.

atan(x, /)
    Return the arc tangent (measured in radians) of x.

    The result is between -pi/2 and pi/2.

atan2(y, x, /)
    Return the arc tangent (measured in radians) of y/x.

    Unlike atan(y/x), the signs of both x and y are considered.

atanh(x, /)
    Return the inverse hyperbolic tangent of x.

ceil(x, /)
    Return the ceiling of x as an Integral.

    This is the smallest integer >= x.
        
SyntaxError: invalid syntax
acosh(x, /)
    Return the inverse hyperbolic cosine of x.

asin(x, /)
    Return the arc sine (measured in radians) of x.

    The result is between -pi/2 and pi/2.

asinh(x, /)
    Return the inverse hyperbolic sine of x.

atan(x, /)
    Return the arc tangent (measured in radians) of x.

    The result is between -pi/2 and pi/2.

atan2(y, x, /)
    Return the arc tangent (measured in radians) of y/x.

    Unlike atan(y/x), the signs of both x and y are considered.

atanh(x, /)
    Return the inverse hyperbolic tangent of x.

ceil(x, /)
    Return the ceiling of x as an Integral.

    This is the smallest integer >= x.



import math

tan(45)
Traceback (most recent call last):
  File "<pyshell#1520>", line 1, in <module>
    tan(45)
NameError: name 'tan' is not defined






math.tan(90)
-1.995200412208242


math.tan945)
SyntaxError: unmatched ')'
math.tan(45)
1.6197751905438615



math.sqrt(9)
3.0


math,oi
Traceback (most recent call last):
  File "<pyshell#1537>", line 1, in <module>
    math,oi
NameError: name 'oi' is not defined. Did you mean: 'i'?
math.pi
3.141592653589793





variable_list=dir('math')
variable_list
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



print(variable_list)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']






print(variable_list,sep='\n')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']





['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

d
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'inf'
'inf'





dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        
        The result is between 0 and pi.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(*integers)
        Greatest Common Divisor.
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    lcm(*integers)
        Least Common Multiple.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    nextafter(x, y, /)
        Return the next floating-point value after x towards y.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.
    
    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


append
Traceback (most recent call last):
  File "<pyshell#1567>", line 1, in <module>
    append
NameError: name 'append' is not defined


class_info, variable_info, function_info = []
Traceback (most recent call last):
  File "<pyshell#1569>", line 1, in <module>
    class_info, variable_info, function_info = []
ValueError: not enough values to unpack (expected 3, got 0)
class_info, variable_info, function_info = [],[],[]






a=input()
goli
a
'goli'





type(a)
<class 'str'>


b=input()
10
b
'10'

type(b)
<class 'str'>


a,b,c=input()
10,20,30
Traceback (most recent call last):
  File "<pyshell#1592>", line 1, in <module>
    a,b,c=input()
ValueError: too many values to unpack (expected 3)
type(a)
<class 'str'>
a,b,c=input()
10 20 30
Traceback (most recent call last):
  File "<pyshell#1594>", line 1, in <module>
    a,b,c=input()
ValueError: too many values to unpack (expected 3)


dir(map)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.









a,b= [int(x) for x in input('Enter two numbers').splict()]
Enter two numbers10 20
Traceback (most recent call last):
  File "<pyshell#1607>", line 1, in <module>
    a,b= [int(x) for x in input('Enter two numbers').splict()]
AttributeError: 'str' object has no attribute 'splict'. Did you mean: 'split'?
a,b= [int(x) for x in input('Enter two numbers').split()]
Enter two numbers10 20
a
10
b
20



a,b,c=[int(x) for x in input("Enter three numbers:").split()]
Enter three numbers:10 20 30
a
10
b
20
c
30
a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
Enter three numbers:
Traceback (most recent call last):
  File "<pyshell#1617>", line 1, in <module>
    a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
  File "<pyshell#1617>", line 1, in <listcomp>
    a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
ValueError: invalid literal for int() with base 10: ''
a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
Enter three numbers:10,20,30
a
10
b
20
c
30



a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
Enter three numbers:100,200,300
a
100
b
200
c
300
a,b,c
(100, 200, 300)

a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
Enter three numbers:300 200 100 
Traceback (most recent call last):
  File "<pyshell#1631>", line 1, in <module>
    a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
  File "<pyshell#1631>", line 1, in <listcomp>
    a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
ValueError: invalid literal for int() with base 10: '300 200 100 '



try:
    a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
except ValueError:
    print('Invalid separator entered')

    
Enter three numbers:200 300 400
Invalid separator entered
try:
    a,b,c=[int(x) for x in input("Enter three numbers:").split(',')]
except ValueError:
    print('Invalid separator entered')

    
Enter three numbers:300,400,500
a
300
a,b,c
(300, 400, 500)



help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.


input_string=input("Enter three numbers:")
Enter three numbers:4,5,6
a,b,c=[int(x) for x in input_string.split(',')]
a,b,c
(4, 5, 6)





input_string=input("Enter three numbers:")
Enter three numbers:10,20,30
a,b,c=map(int,input_string.split(','))
a,b,c
(10, 20, 30)






a,b,c=map(int,input('Enter three values:').split(','))
Enter three values:10,20,30
a,b,c
(10, 20, 30)
a,b,c=map(int,input('Enter three values:').split(','))
Enter three values:10,100,1000
a,b,c
(10, 100, 1000)



a,b,c=[int(x) for x in input('Enter vales').split()]
Enter vales10 20 30
a,b,c
(10, 20, 30)

type(input_string)
<class 'str'>


|  __new__(*args, **kwargs) from builtins.type
SyntaxError: invalid syntax
|  __new__(*args, **kwargs) from builtins.type





help(eval)
Help on built-in function eval in module builtins:

eval(source, globals=None, locals=None, /)
    Evaluate the given source in the context of globals and locals.
    
    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.

"3+4"
'3+4'



'3+4'
'3+4'

eval("3+4")
7
