Types of datatypes/ object types
Number:
int # integer
float # floating point number
boolean # True or False
complex # complex number
decimal # decimal number
fractional # fractional number
None # NoneType

string:
list [] # list
tuple () # tuple
dict {} # dictionary
set {} # set
tuples () # tuple

file: 
open('file.txt', 'r') as f:
    data = f.read()
    print(data)

[] = brackets
() = paranthesis
{} = curly paranthesis

Functions:
def function_name(parameters):
    # function body
    return value

Modules:
import module_name  
import module_name as alias
from module_name import function_name
from module_name import *
from module_name import function_name as alias

Decorators:
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

Generators:
def generator_function():
    yield 1
    yield 2
    yield 3

Iterators:

Meta programming:
class Meta(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)


Note: dir(object_name) # returns the list of attributes and methods of the object
