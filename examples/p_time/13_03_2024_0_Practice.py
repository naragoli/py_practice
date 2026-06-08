Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
hi
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hi
NameError: name 'hi' is not defined



a,b,c=[int(x) for x in input('Enter three inputs:').split()]
Enter three inputs:10 20 30
ab,c
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ab,c
NameError: name 'ab' is not defined. Did you mean: 'a'?
a,b,c
(10, 20, 30)


y=[100,200,300]

a,b,c=[int(x) for x in y.split()]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a,b,c=[int(x) for x in y.split()]
AttributeError: 'list' object has no attribute 'split'
a,b,c=[int(x) for x in y]
a,b,c
(100, 200, 300)
a
100
b
200
c
300



min= a if a<b and a<c else b if b<c else c
min
100
min= a if a<b and a<c else(b if b<c else c)
min
100


a,b,c=300,200,100
a,b,c
(300, 200, 100)




min= a if a<b and a<c else(b if b<c else c)
min
100



a,b,c=100,200,300
a,b,c
(100, 200, 300)




max = a if a>b and a>c else (b if b>C else c)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    max = a if a>b and a>c else (b if b>C else c)
NameError: name 'C' is not defined. Did you mean: 'c'?
max = a if a>b and a>c else (b if b>c else c)
max
300









import keywords
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
ModuleNotFoundError: No module named 'keywords'
SyntaxError: invalid syntax


import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']



import inspect
import importlib

module_name=input('Enter a module name:')
Enter a module name:math
class_info,variable_info,function_info = [],[],[]
module_members=inspect.importlib(module_name)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    module_members=inspect.importlib(module_name)
TypeError: 'module' object is not callable
module=importlib.import_module(module_name)
module_members=inspect.getmembers(module)

type(module)
<class 'module'>
module
<module 'math' (built-in)>
print(module)
<module 'math' (built-in)>



module[0]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    module[0]
TypeError: 'module' object is not subscriptable
for member in module
SyntaxError: expected ':'
for member in module:
    print(member)

    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    for member in module:
TypeError: 'module' object is not iterable
module_members
[('__doc__', 'This module provides access to the mathematical functions\ndefined by the C standard.'), ('__loader__', <class '_frozen_importlib.BuiltinImporter'>), ('__name__', 'math'), ('__package__', ''), ('__spec__', ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')), ('acos', <built-in function acos>), ('acosh', <built-in function acosh>), ('asin', <built-in function asin>), ('asinh', <built-in function asinh>), ('atan', <built-in function atan>), ('atan2', <built-in function atan2>), ('atanh', <built-in function atanh>), ('ceil', <built-in function ceil>), ('comb', <built-in function comb>), ('copysign', <built-in function copysign>), ('cos', <built-in function cos>), ('cosh', <built-in function cosh>), ('degrees', <built-in function degrees>), ('dist', <built-in function dist>), ('e', 2.718281828459045), ('erf', <built-in function erf>), ('erfc', <built-in function erfc>), ('exp', <built-in function exp>), ('expm1', <built-in function expm1>), ('fabs', <built-in function fabs>), ('factorial', <built-in function factorial>), ('floor', <built-in function floor>), ('fmod', <built-in function fmod>), ('frexp', <built-in function frexp>), ('fsum', <built-in function fsum>), ('gamma', <built-in function gamma>), ('gcd', <built-in function gcd>), ('hypot', <built-in function hypot>), ('inf', inf), ('isclose', <built-in function isclose>), ('isfinite', <built-in function isfinite>), ('isinf', <built-in function isinf>), ('isnan', <built-in function isnan>), ('isqrt', <built-in function isqrt>), ('lcm', <built-in function lcm>), ('ldexp', <built-in function ldexp>), ('lgamma', <built-in function lgamma>), ('log', <built-in function log>), ('log10', <built-in function log10>), ('log1p', <built-in function log1p>), ('log2', <built-in function log2>), ('modf', <built-in function modf>), ('nan', nan), ('nextafter', <built-in function nextafter>), ('perm', <built-in function perm>), ('pi', 3.141592653589793), ('pow', <built-in function pow>), ('prod', <built-in function prod>), ('radians', <built-in function radians>), ('remainder', <built-in function remainder>), ('sin', <built-in function sin>), ('sinh', <built-in function sinh>), ('sqrt', <built-in function sqrt>), ('tan', <built-in function tan>), ('tanh', <built-in function tanh>), ('tau', 6.283185307179586), ('trunc', <built-in function trunc>), ('ulp', <built-in function ulp>)]



type(module_members)
<class 'list'>




type(module_members[0])
<class 'tuple'>



for member in module_members:
    print(member,sep='\n')

    
('__doc__', 'This module provides access to the mathematical functions\ndefined by the C standard.')
('__loader__', <class '_frozen_importlib.BuiltinImporter'>)
('__name__', 'math')
('__package__', '')
('__spec__', ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'))
('acos', <built-in function acos>)
('acosh', <built-in function acosh>)
('asin', <built-in function asin>)
('asinh', <built-in function asinh>)
('atan', <built-in function atan>)
('atan2', <built-in function atan2>)
('atanh', <built-in function atanh>)
('ceil', <built-in function ceil>)
('comb', <built-in function comb>)
('copysign', <built-in function copysign>)
('cos', <built-in function cos>)
('cosh', <built-in function cosh>)
('degrees', <built-in function degrees>)
('dist', <built-in function dist>)
('e', 2.718281828459045)
('erf', <built-in function erf>)
('erfc', <built-in function erfc>)
('exp', <built-in function exp>)
('expm1', <built-in function expm1>)
('fabs', <built-in function fabs>)
('factorial', <built-in function factorial>)
('floor', <built-in function floor>)
('fmod', <built-in function fmod>)
('frexp', <built-in function frexp>)
('fsum', <built-in function fsum>)
('gamma', <built-in function gamma>)
('gcd', <built-in function gcd>)
('hypot', <built-in function hypot>)
('inf', inf)
('isclose', <built-in function isclose>)
('isfinite', <built-in function isfinite>)
('isinf', <built-in function isinf>)
('isnan', <built-in function isnan>)
('isqrt', <built-in function isqrt>)
('lcm', <built-in function lcm>)
('ldexp', <built-in function ldexp>)
('lgamma', <built-in function lgamma>)
('log', <built-in function log>)
('log10', <built-in function log10>)
('log1p', <built-in function log1p>)
('log2', <built-in function log2>)
('modf', <built-in function modf>)
('nan', nan)
('nextafter', <built-in function nextafter>)
('perm', <built-in function perm>)
('pi', 3.141592653589793)
('pow', <built-in function pow>)
('prod', <built-in function prod>)
('radians', <built-in function radians>)
('remainder', <built-in function remainder>)
('sin', <built-in function sin>)
('sinh', <built-in function sinh>)
('sqrt', <built-in function sqrt>)
('tan', <built-in function tan>)
('tanh', <built-in function tanh>)
('tau', 6.283185307179586)
('trunc', <built-in function trunc>)
('ulp', <built-in function ulp>)
('dist', <built-in function dist>)
SyntaxError: invalid syntax


for member in module_members:
    if inspect.isclass(member[1]):
        class_info.append(member[0])
    elif inspect.isfunction(member[1]):
        function_info.append(member[0])
    else:
        variable_info.append(member[0]
                             
KeyboardInterrupt
class_info
                             
[]
for member in module_members:
    if inspect.isclass(member[1]):
        class_info.append(member[0])
    elif inspect.isfunction(member[1]):
        function_info.append(member[0])
    else:
        variable_info.append(member[0]
                             
KeyboardInterrupt
module=importlib.import_module(module_name)
module_members=inspect.getmembers(module)
                             
SyntaxError: multiple statements found while compiling a single statement






a='narasimha goli'
                             
type(a)
                             
<class 'str'>




a[0[
    a

    
KeyboardInterrupt
a[0]
    
'n'


a[0]=N
    
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    a[0]=N
NameError: name 'N' is not defined








import sys
type(argv)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    type(argv)
NameError: name 'argv' is not defined


print(type(argv))
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    print(type(argv))
NameError: name 'argv' is not defined


import argv
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    import argv
ModuleNotFoundError: No module named 'argv'
import argv from sys
SyntaxError: invalid syntax


from sys import argv


type(argv)
<class 'list'>



print(argv)
['']









time
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    time
NameError: name 'time' is not defined


date
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    date
NameError: name 'date' is not defined





hi
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    hi
NameError: name 'hi' is not defined




10
10
10+20
30



print(goli*10)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    print(goli*10)
NameError: name 'goli' is not defined
print('goli'*10)
goligoligoligoligoligoligoligoligoligoli
print('goli'*10,sep='\n')
goligoligoligoligoligoligoligoligoligoli
print('goli'*10,end='\n')
goligoligoligoligoligoligoligoligoligoli
print('goli'+'Goli')
goliGoli


print('Goli'-'li')
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    print('Goli'-'li')
TypeError: unsupported operand type(s) for -: 'str' and 'str'





a,b,c=10,20,30
    
print(" a value is %i",%a)
    
SyntaxError: invalid syntax
print(" a value is %i" %a)
    
 a value is 10
s=[100,200,300]
    
print("S is a list with:" %s)
    
S is a list with:
s
    
[100, 200, 300]


print("S is a list with:" %s)
    
S is a list with:
print("s is a list with:" %s)
    
s is a list with:
%s
    
SyntaxError: invalid syntax




s
    
[100, 200, 300]



print("s is a list with content %s" ,%s)
    
SyntaxError: invalid syntax
print("s is a list with content %s" %s)
    
s is a list with content [100, 200, 300]







b=s
    
b
    
[100, 200, 300]





print(" b is a list with content %s" %b)
    
 b is a list with content [100, 200, 300]





a,b,c
    
(10, [100, 200, 300], 30)
a,b,c=10,20,30
    



a,b,c
    
(10, 20, 30)




print("Value of a: {} and value of b: {} and value of c: {}".format(a,b,c))
    
Value of a: 10 and value of b: 20 and value of c: 30
print("Value of a: {0} and value of b: {1} and value of c: {2}".format(a,b,c))
    
Value of a: 10 and value of b: 20 and value of c: 30



print("Value of a: {2} and value of b: {1} and value of c: {0}".format(a,b,c))
    
Value of a: 30 and value of b: 20 and value of c: 10


print("Value of a: {x} and value of b: {y} and value of c: {z}".format(x=a,y=b,z=c))
    
Value of a: 10 and value of b: 20 and value of c: 30




for item in range(1,10,1):
    print("{} x {} = {}".format(item,int(item)+1,int(item)*int(item)+))
    
SyntaxError: invalid syntax


for item in range(1,10,1):
    print("{} x {} = {}".format(item,int(item)+1,int(item)*int(item)+1))

    
1 x 2 = 2
2 x 3 = 5
3 x 4 = 10
4 x 5 = 17
5 x 6 = 26
6 x 7 = 37
7 x 8 = 50
8 x 9 = 65
9 x 10 = 82

for item in range(1,10):
    print("{} x {} = {}".format(item,int(item)+1,int(item)*int(item)+1))

    
1 x 2 = 2
2 x 3 = 5
3 x 4 = 10
4 x 5 = 17
5 x 6 = 26
6 x 7 = 37
7 x 8 = 50
8 x 9 = 65
9 x 10 = 82
for item in range(1,10):
    print("{} x {} = {}".format(2,int(item)+1,int(item)*int(item)+1))

    
2 x 2 = 2
2 x 3 = 5
2 x 4 = 10
2 x 5 = 17
2 x 6 = 26
2 x 7 = 37
2 x 8 = 50
2 x 9 = 65
2 x 10 = 82
for item in range(1,10):
    print("{} x {} = {}".format(2,int(item),int(item)*int(item)+1))

    
2 x 1 = 2
2 x 2 = 5
2 x 3 = 10
2 x 4 = 17
2 x 5 = 26
2 x 6 = 37
2 x 7 = 50
2 x 8 = 65
2 x 9 = 82
for item in range(1,10):
    print("{} x {} = {}".format(2,int(item),2*int(item)))

    
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18



dir('argparser')
    
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']




help(argparser)
    
Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    help(argparser)
NameError: name 'argparser' is not defined
help('argparser')
    
No Python documentation found for 'argparser'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help('argparse')
    
Help on module argparse:

NAME
    argparse - Command-line parsing library

MODULE REFERENCE
    https://docs.python.org/3.10/library/argparse.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is an optparse-inspired command-line parsing library that:
    
        - handles both optional and positional arguments
        - produces highly informative usage messages
        - supports parsers that dispatch to sub-parsers
    
    The following is a simple usage example that sums integers from the
    command-line and writes the result to a file::
    
        parser = argparse.ArgumentParser(
            description='sum the integers at the command line')
        parser.add_argument(
            'integers', metavar='int', nargs='+', type=int,
            help='an integer to be summed')
        parser.add_argument(
            '--log', default=sys.stdout, type=argparse.FileType('w'),
            help='the file where the sum should be written')
        args = parser.parse_args()
        args.log.write('%s' % sum(args.integers))
        args.log.close()
    
    The module contains the following public classes:
    
        - ArgumentParser -- The main entry point for command-line parsing. As the
            example above shows, the add_argument() method is used to populate
            the parser with actions for optional and positional arguments. Then
            the parse_args() method is invoked to convert the args at the
            command-line into an object with attributes.
    
        - ArgumentError -- The exception raised by ArgumentParser objects when
            there are errors with the parser's actions. Errors raised while
            parsing the command-line are caught by ArgumentParser and emitted
            as command-line messages.
    
        - FileType -- A factory for defining types of files to be created. As the
            example above shows, instances of FileType are typically passed as
            the type= argument of add_argument() calls.
    
        - Action -- The base class for parser actions. Typically actions are
            selected by passing strings like 'store_true' or 'append_const' to
            the action= argument of add_argument(). However, for greater
            customization of ArgumentParser actions, subclasses of Action may
            be defined and passed as the action= argument.
    
        - HelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter,
            ArgumentDefaultsHelpFormatter -- Formatter classes which
            may be passed as the formatter_class= argument to the
            ArgumentParser constructor. HelpFormatter is the default,
            RawDescriptionHelpFormatter and RawTextHelpFormatter tell the parser
            not to change the formatting for help text, and
            ArgumentDefaultsHelpFormatter adds information about argument defaults
            to the help.
    
    All other classes in this module are considered implementation details.
    (Also note that HelpFormatter and RawDescriptionHelpFormatter are only
    considered public as object names -- the API of the formatter objects is
    still considered an implementation detail.)

CLASSES
    _ActionsContainer(builtins.object)
        ArgumentParser(_AttributeHolder, _ActionsContainer)
    _AttributeHolder(builtins.object)
        Action
            BooleanOptionalAction
        ArgumentParser(_AttributeHolder, _ActionsContainer)
        Namespace
    builtins.Exception(builtins.BaseException)
        ArgumentError
        ArgumentTypeError
    builtins.object
        FileType
        HelpFormatter
            ArgumentDefaultsHelpFormatter
            MetavarTypeHelpFormatter
            RawDescriptionHelpFormatter
                RawTextHelpFormatter
    
    class Action(_AttributeHolder)
     |  Action(option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None)
     |  
     |  Information about how to convert command line strings to Python objects.
     |  
     |  Action objects are used by an ArgumentParser to represent the information
     |  needed to parse a single argument from one or more strings from the
     |  command line. The keyword arguments to the Action constructor are also
     |  all attributes of Action instances.
     |  
     |  Keyword Arguments:
     |  
     |      - option_strings -- A list of command-line option strings which
     |          should be associated with this action.
     |  
     |      - dest -- The name of the attribute to hold the created object(s)
     |  
     |      - nargs -- The number of command-line arguments that should be
     |          consumed. By default, one argument will be consumed and a single
     |          value will be produced.  Other values include:
     |              - N (an integer) consumes N arguments (and produces a list)
     |              - '?' consumes zero or one arguments
     |              - '*' consumes zero or more arguments (and produces a list)
     |              - '+' consumes one or more arguments (and produces a list)
     |          Note that the difference between the default and nargs=1 is that
     |          with the default, a single value will be produced, while with
     |          nargs=1, a list containing a single value will be produced.
     |  
     |      - const -- The value to be produced if the option is specified and the
     |          option uses an action that takes no values.
     |  
     |      - default -- The value to be produced if the option is not specified.
     |  
     |      - type -- A callable that accepts a single string argument, and
     |          returns the converted value.  The standard Python types str, int,
     |          float, and complex are useful examples of such callables.  If None,
     |          str is used.
     |  
     |      - choices -- A container of values that should be allowed. If not None,
     |          after a command-line argument has been converted to the appropriate
     |          type, an exception will be raised if it is not a member of this
     |          collection.
     |  
     |      - required -- True if the action must always be specified at the
     |          command line. This is only meaningful for optional command-line
     |          arguments.
     |  
     |      - help -- The help string describing the argument.
     |  
     |      - metavar -- The name to be used for the option's argument with the
     |          help string. If None, the 'dest' value will be used as the name.
     |  
     |  Method resolution order:
     |      Action
     |      _AttributeHolder
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __call__(self, parser, namespace, values, option_string=None)
     |      Call self as a function.
     |  
     |  __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  format_usage(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _AttributeHolder:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _AttributeHolder:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class ArgumentDefaultsHelpFormatter(HelpFormatter)
     |  ArgumentDefaultsHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)
     |  
     |  Help message formatter which adds default values to argument help.
     |  
     |  Only the name of this class is considered a public API. All the methods
     |  provided by the class are considered an implementation detail.
     |  
     |  Method resolution order:
     |      ArgumentDefaultsHelpFormatter
     |      HelpFormatter
     |      builtins.object
     |  
     |  Methods inherited from HelpFormatter:
     |  
     |  __init__(self, prog, indent_increment=2, max_help_position=24, width=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_argument(self, action)
     |  
     |  add_arguments(self, actions)
     |  
     |  add_text(self, text)
     |  
     |  add_usage(self, usage, actions, groups, prefix=None)
     |  
     |  end_section(self)
     |  
     |  format_help(self)
     |      # =======================
     |      # Help-formatting methods
     |      # =======================
     |  
     |  start_section(self, heading)
     |      # ========================
     |      # Message building methods
     |      # ========================
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from HelpFormatter:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class ArgumentError(builtins.Exception)
     |  ArgumentError(argument, message)
     |  
     |  An error from creating or using an argument (optional or positional).
     |  
     |  The string value of this exception is the message, augmented with
     |  information about the argument that caused it.
     |  
     |  Method resolution order:
     |      ArgumentError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, argument, message)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __str__(self)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class ArgumentParser(_AttributeHolder, _ActionsContainer)
     |  ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=<class 'argparse.HelpFormatter'>, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)
     |  
     |  Object for parsing command line strings into Python objects.
     |  
     |  Keyword Arguments:
     |      - prog -- The name of the program (default:
     |          ``os.path.basename(sys.argv[0])``)
     |      - usage -- A usage message (default: auto-generated from arguments)
     |      - description -- A description of what the program does
     |      - epilog -- Text following the argument descriptions
     |      - parents -- Parsers whose arguments should be copied into this one
     |      - formatter_class -- HelpFormatter class for printing help messages
     |      - prefix_chars -- Characters that prefix optional arguments
     |      - fromfile_prefix_chars -- Characters that prefix files containing
     |          additional arguments
     |      - argument_default -- The default value for all arguments
     |      - conflict_handler -- String indicating how to handle conflicts
     |      - add_help -- Add a -h/-help option
     |      - allow_abbrev -- Allow long options to be abbreviated unambiguously
     |      - exit_on_error -- Determines whether or not ArgumentParser exits with
     |          error info when an error occurs
     |  
     |  Method resolution order:
     |      ArgumentParser
     |      _AttributeHolder
     |      _ActionsContainer
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=<class 'argparse.HelpFormatter'>, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_subparsers(self, **kwargs)
     |      # ==================================
     |      # Optional/Positional adding methods
     |      # ==================================
     |  
     |  convert_arg_line_to_args(self, arg_line)
     |  
     |  error(self, message)
     |      error(message: string)
     |      
     |      Prints a usage message incorporating the message to stderr and
     |      exits.
     |      
     |      If you override this in a subclass, it should not return -- it
     |      should either exit or raise an exception.
     |  
     |  exit(self, status=0, message=None)
     |      # ===============
     |      # Exiting methods
     |      # ===============
     |  
     |  format_help(self)
     |  
     |  format_usage(self)
     |      # =======================
     |      # Help-formatting methods
     |      # =======================
     |  
     |  parse_args(self, args=None, namespace=None)
     |      # =====================================
     |      # Command line argument parsing methods
     |      # =====================================
     |  
     |  parse_intermixed_args(self, args=None, namespace=None)
     |  
     |  parse_known_args(self, args=None, namespace=None)
     |  
     |  parse_known_intermixed_args(self, args=None, namespace=None)
     |  
     |  print_help(self, file=None)
     |  
     |  print_usage(self, file=None)
     |      # =====================
     |      # Help-printing methods
     |      # =====================
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _AttributeHolder:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _AttributeHolder:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _ActionsContainer:
     |  
     |  add_argument(self, *args, **kwargs)
     |      add_argument(dest, ..., name=value, ...)
     |      add_argument(option_string, option_string, ..., name=value, ...)
     |  
     |  add_argument_group(self, *args, **kwargs)
     |  
     |  add_mutually_exclusive_group(self, **kwargs)
     |  
     |  get_default(self, dest)
     |  
     |  register(self, registry_name, value, object)
     |      # ====================
     |      # Registration methods
     |      # ====================
     |  
     |  set_defaults(self, **kwargs)
     |      # ==================================
     |      # Namespace default accessor methods
     |      # ==================================
    
    class ArgumentTypeError(builtins.Exception)
     |  An error from trying to convert a command line string to a type.
     |  
     |  Method resolution order:
     |      ArgumentTypeError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class BooleanOptionalAction(Action)
     |  BooleanOptionalAction(option_strings, dest, default=None, type=None, choices=None, required=False, help=None, metavar=None)
     |  
     |  Method resolution order:
     |      BooleanOptionalAction
     |      Action
     |      _AttributeHolder
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __call__(self, parser, namespace, values, option_string=None)
     |      Call self as a function.
     |  
     |  __init__(self, option_strings, dest, default=None, type=None, choices=None, required=False, help=None, metavar=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  format_usage(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _AttributeHolder:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _AttributeHolder:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class FileType(builtins.object)
     |  FileType(mode='r', bufsize=-1, encoding=None, errors=None)
     |  
     |  Factory for creating file object types
     |  
     |  Instances of FileType are typically passed as type= arguments to the
     |  ArgumentParser add_argument() method.
     |  
     |  Keyword Arguments:
     |      - mode -- A string indicating how the file is to be opened. Accepts the
     |          same values as the builtin open() function.
     |      - bufsize -- The file's desired buffer size. Accepts the same values as
     |          the builtin open() function.
     |      - encoding -- The file's encoding. Accepts the same values as the
     |          builtin open() function.
     |      - errors -- A string indicating how encoding and decoding errors are to
     |          be handled. Accepts the same value as the builtin open() function.
     |  
     |  Methods defined here:
     |  
     |  __call__(self, string)
     |      Call self as a function.
     |  
     |  __init__(self, mode='r', bufsize=-1, encoding=None, errors=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class HelpFormatter(builtins.object)
     |  HelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)
     |  
     |  Formatter for generating usage messages and argument help strings.
     |  
     |  Only the name of this class is considered a public API. All the methods
     |  provided by the class are considered an implementation detail.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, prog, indent_increment=2, max_help_position=24, width=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_argument(self, action)
     |  
     |  add_arguments(self, actions)
     |  
     |  add_text(self, text)
     |  
     |  add_usage(self, usage, actions, groups, prefix=None)
     |  
     |  end_section(self)
     |  
     |  format_help(self)
     |      # =======================
     |      # Help-formatting methods
     |      # =======================
     |  
     |  start_section(self, heading)
     |      # ========================
     |      # Message building methods
     |      # ========================
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class MetavarTypeHelpFormatter(HelpFormatter)
     |  MetavarTypeHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)
     |  
     |  Help message formatter which uses the argument 'type' as the default
     |  metavar value (instead of the argument 'dest')
     |  
     |  Only the name of this class is considered a public API. All the methods
     |  provided by the class are considered an implementation detail.
     |  
     |  Method resolution order:
     |      MetavarTypeHelpFormatter
     |      HelpFormatter
     |      builtins.object
     |  
     |  Methods inherited from HelpFormatter:
     |  
     |  __init__(self, prog, indent_increment=2, max_help_position=24, width=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_argument(self, action)
     |  
     |  add_arguments(self, actions)
     |  
     |  add_text(self, text)
     |  
     |  add_usage(self, usage, actions, groups, prefix=None)
     |  
     |  end_section(self)
     |  
     |  format_help(self)
     |      # =======================
     |      # Help-formatting methods
     |      # =======================
     |  
     |  start_section(self, heading)
     |      # ========================
     |      # Message building methods
     |      # ========================
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from HelpFormatter:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Namespace(_AttributeHolder)
     |  Namespace(**kwargs)
     |  
     |  Simple object for storing attributes.
     |  
     |  Implements equality by attribute names and values, and provides a simple
     |  string representation.
     |  
     |  Method resolution order:
     |      Namespace
     |      _AttributeHolder
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __contains__(self, key)
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  __init__(self, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _AttributeHolder:
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _AttributeHolder:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class RawDescriptionHelpFormatter(HelpFormatter)
     |  RawDescriptionHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)
     |  
     |  Help message formatter which retains any formatting in descriptions.
     |  
     |  Only the name of this class is considered a public API. All the methods
     |  provided by the class are considered an implementation detail.
     |  
     |  Method resolution order:
     |      RawDescriptionHelpFormatter
     |      HelpFormatter
     |      builtins.object
     |  
     |  Methods inherited from HelpFormatter:
     |  
     |  __init__(self, prog, indent_increment=2, max_help_position=24, width=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_argument(self, action)
     |  
     |  add_arguments(self, actions)
     |  
     |  add_text(self, text)
     |  
     |  add_usage(self, usage, actions, groups, prefix=None)
     |  
     |  end_section(self)
     |  
     |  format_help(self)
     |      # =======================
     |      # Help-formatting methods
     |      # =======================
     |  
     |  start_section(self, heading)
     |      # ========================
     |      # Message building methods
     |      # ========================
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from HelpFormatter:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class RawTextHelpFormatter(RawDescriptionHelpFormatter)
     |  RawTextHelpFormatter(prog, indent_increment=2, max_help_position=24, width=None)
     |  
     |  Help message formatter which retains formatting of all help text.
     |  
     |  Only the name of this class is considered a public API. All the methods
     |  provided by the class are considered an implementation detail.
     |  
     |  Method resolution order:
     |      RawTextHelpFormatter
     |      RawDescriptionHelpFormatter
     |      HelpFormatter
     |      builtins.object
     |  
     |  Methods inherited from HelpFormatter:
     |  
     |  __init__(self, prog, indent_increment=2, max_help_position=24, width=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_argument(self, action)
     |  
     |  add_arguments(self, actions)
     |  
     |  add_text(self, text)
     |  
     |  add_usage(self, usage, actions, groups, prefix=None)
     |  
     |  end_section(self)
     |  
     |  format_help(self)
     |      # =======================
     |      # Help-formatting methods
     |      # =======================
     |  
     |  start_section(self, heading)
     |      # ========================
     |      # Message building methods
     |      # ========================
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from HelpFormatter:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

DATA
    ONE_OR_MORE = '+'
    OPTIONAL = '?'
    PARSER = 'A...'
    REMAINDER = '...'
    SUPPRESS = '==SUPPRESS=='
    ZERO_OR_MORE = '*'
    __all__ = ['ArgumentParser', 'ArgumentError', 'ArgumentTypeError', 'Bo...

VERSION
    1.1

FILE
    c:\users\avadh\appdata\local\programs\python\python310\lib\argparse.py


parser.parse_args()
               
Traceback (most recent call last):
  File "<pyshell#296>", line 1, in <module>
    parser.parse_args()
NameError: name 'parser' is not defined




4%2
               
0



5%2
               
1















for x in range(1:11):
               
SyntaxError: expected ':'
for x in range(1,11):
               print(x)

               
1
2
3
4
5
6
7
8
9
10
for x in range(1,21,1):
               if ((x%2)!=0):
               print(x)
               
SyntaxError: expected an indented block after 'if' statement on line 2
for x in range(1,21,1):
               if ((x%2)!=0):
                   print(x)

               
1
3
5
7
9
11
13
15
17
19
for x in range(1,21,1):
               if ((x%2)=0):
                   print(x)
               
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
for x in range(1,21,1):
               if ((x%2)==0):
                   print(x)

               
2
4
6
8
10
12
14
16
18
20
range(10,0)
               
range(10, 0)




for x in range(10,0):
               print(x)

               


for x in range(10,0,-1):
               print(x)

               
10
9
8
7
6
5
4
3
2
1
12
               
12









list=eval(inputs('Enter a list : '))
               
Traceback (most recent call last):
  File "<pyshell#341>", line 1, in <module>
    list=eval(inputs('Enter a list : '))
NameError: name 'inputs' is not defined. Did you mean: 'input'?
list=eval(input('Enter a list : '))
               
Enter a list : [10,20,30]
list
               
[10, 20, 30]


type(list)
               
<class 'list'>



sum=0
               
for x in list:
               sum+=x
            print(sum)
               
SyntaxError: unindent does not match any outer indentation level
for x in list:
               sum+=x
        print(sum)
               
SyntaxError: unindent does not match any outer indentation level
for x in list:
               sum+=x
                print(sum)
               
SyntaxError: unexpected indent
for x in list:
    sum+=x
print(sum)
               
SyntaxError: invalid syntax
for x in list:
               sum+=x
print(sum)
               
SyntaxError: invalid syntax
for x in list:
               sum+=x
               print(sum)

               
10
30
60
for x in list:
               sum+=x

               print(sum)

               
70
90
120
sum=0
               
for x in list:
               sum+=x

print(sum)
               
SyntaxError: invalid syntax







x=1
               
whil1 x<=10:
               
SyntaxError: invalid syntax
x=1
               
while x<=10:
    print(x)
    x+=1

    
1
2
3
4
5
6
7
8
9
10



n=int(input('Enter number :'))
Enter number :50
sum=0
temp=1
while temp <= n:
    sum+=temp
    temp+=1

    


print(sum)
1275


n=int(input('Enter number :'))
Enter number :20
sum=0
temp=1
while temp <= n:
    sum+=temp
    temp+=1

    


print(sum)
SyntaxError: multiple statements found while compiling a single statement
sum=0
temp=1
while temp <= n:
    sum+=temp
    temp+=1
print(sum)
SyntaxError: multiple statements found while compiling a single statement
sum=0
temp=1
while temp <= n:
    sum+=temp
    temp+=1
print(sum)
SyntaxError: multiple statements found while compiling a single statement










name=""
while name != 'Goli':
    name=input('Enter the name')
print('name is goli')
SyntaxError: invalid syntax
name=""
while name != 'Goli':
    name=input('Enter the name')
    
SyntaxError: multiple statements found while compiling a single statement
name=""
while name != 'Goli':
    name=input('Enter the name')

    
Enter the namehi
Enter the namehi
Enter the namegoli
Enter the nameGoli



for i in range(4):
    for j in range(4)
    
SyntaxError: expected ':'
for i in range(4):
    for j in range(4):
        print(i,j)

        
0 0
0 1
0 2
0 3
1 0
1 1
1 2
1 3
2 0
2 1
2 2
2 3
3 0
3 1
3 2
3 3








help(pass)
SyntaxError: invalid syntax


help('pass)
     
SyntaxError: unterminated string literal (detected at line 1)
help('pass')
     
The "pass" statement
********************

   pass_stmt ::= "pass"

"pass" is a null operation — when it is executed, nothing happens. It
is useful as a placeholder when a statement is required syntactically,
but no code needs to be executed, for example:

   def f(arg): pass    # a function that does nothing (yet)

   class C: pass       # a class with no methods (yet)






for i in range(10):
    if i%2 == 0:
        print(i)
    else: pass

    
0
2
4
6
8




x=10
id(x)
2696290370064
print(x)
10


del(x)


x
Traceback (most recent call last):
  File "<pyshell#454>", line 1, in <module>
    x
NameError: name 'x' is not defined




id(x)
Traceback (most recent call last):
  File "<pyshell#459>", line 1, in <module>
    id(x)
NameError: name 'x' is not defined


lis1
Traceback (most recent call last):
  File "<pyshell#462>", line 1, in <module>
    lis1
NameError: name 'lis1' is not defined. Did you mean: 'list'?
list1
Traceback (most recent call last):
  File "<pyshell#463>", line 1, in <module>
    list1
NameError: name 'list1' is not defined. Did you mean: 'list'?


l1
Traceback (most recent call last):
  File "<pyshell#466>", line 1, in <module>
    l1
NameError: name 'l1' is not defined




list1=[10,20,30,40]
     
list1
     
[10, 20, 30, 40]


del(list[0])
     
list
     
[20, 30]
liar
     
Traceback (most recent call last):
  File "<pyshell#477>", line 1, in <module>
    liar
NameError: name 'liar' is not defined
list
     
[20, 30]


list1
     
[10, 20, 30, 40]








del(list1[0])
     
list1
     
[20, 30, 40]



s= 'Narasimha Goli'
     
del(s[4])
     
Traceback (most recent call last):
  File "<pyshell#495>", line 1, in <module>
    del(s[4])
TypeError: 'str' object doesn't support item deletion





del(s)
     
s
     
Traceback (most recent call last):
  File "<pyshell#501>", line 1, in <module>
    s
NameError: name 's' is not defined



s=""" This is goli from
mirylaguda"""
     
s
     
' This is goli from\nmirylaguda'


print(s)
     
 This is goli from
mirylaguda





s='NarasimhaGolifromMiryalaguda'
     
len(s)
     
28



print(s)
     
NarasimhaGolifromMiryalaguda




print(s,sep='\n')
     
NarasimhaGolifromMiryalaguda


s[::-1]
     
'adugalayriMmorfiloGahmisaraN'
s[::-1]
     
'adugalayriMmorfiloGahmisaraN'





s[-2:1:1]
     
''
s[-2:1]
     
''
s[-2::]
     
'da'
s[:-2:]
     
'NarasimhaGolifromMiryalagu'
s[:-2:-1]
     
'a'



a
     
10
s
     
'NarasimhaGolifromMiryalaguda'




s[-1]
     
'a'




dir(strip)
     
Traceback (most recent call last):
  File "<pyshell#551>", line 1, in <module>
    dir(strip)
NameError: name 'strip' is not defined


dir('strip')
     
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

dir('str.strip')
     
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



s='  narasimha goli  '
     
s
     
'  narasimha goli  '
pinnt(s)
     
Traceback (most recent call last):
  File "<pyshell#562>", line 1, in <module>
    pinnt(s)
NameError: name 'pinnt' is not defined. Did you mean: 'print'?
print('s')
     
s





s
     
'  narasimha goli  '
print(s)
     
  narasimha goli  





s.rstrip()
     
'  narasimha goli'
s.lstrip()
     
'narasimha goli  '
s.strip()
     
'narasimha goli'


s
     
'  narasimha goli  '
s
     
'  narasimha goli  '




s.find('goli')
     
12
s[12]
     
'g'
s.find('Goli')
     
-1


s.rfind('goli')
     
12
s.index('goli')
     
12

s.index('Goli')
     
Traceback (most recent call last):
  File "<pyshell#595>", line 1, in <module>
    s.index('Goli')
ValueError: substring not found
