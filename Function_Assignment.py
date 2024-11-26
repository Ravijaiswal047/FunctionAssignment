# 1. What is the difference between a function and a method in Python?
""" sol :- Function :-
         A function is a block of code that is defined using the def keyword (or lambda for anonymous functions). 
        It can be called independently and doesn't have to be associated with any object.
        
        Method :-
        A method is a function that is associated with an object, typically an instance of a class. In Python, 
        methods are functions that are defined inside a class and operate on the data contained within the instance 
        of that class (or the class itself for class methods).
        
        
        """

# 2: Explain the concept of function arguments and parameters in Python.
""" SOl : Parameters:
Parameters are the names used in a function definition to specify what values the function expects to receive when it is called.
They act as placeholders for the actual values (arguments) that will be passed into the function.
Example of parameters:
def greet(name, age):  # 'name' and 'age' are parameters
    print(f"Hello {name}, you are {age} years old.")


    Arguments:
Arguments are the actual values that you provide to the function when you call it. These are assigned to the corresponding parameters in the function definition.
Example of arguments:
greet("Alice", 30)  # "Alice" and 30 are arguments

"""

# 3:-  What are the different ways to define and call a function in Python?

"""
Sol : - Calling a Function Inside Another Function
You can call one function from within another. 
This is useful when you want to break down complex logic into smaller, reusable parts.
Example:
def multiply(a, b):
    return a * b

def square(n):
    return multiply(n, n)

result = square(4)  # Calls 'multiply' inside 'square'
print(result)  # Output: 16

# Returning Functions from Functions (Higher-order Functions)
Python allows you to return functions from other functions. 
These are called higher-order functions. 
This is useful when you want to create functions dynamically or return behavior.

Example :-
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_5 = outer_function(5)  # Returns the inner function with x = 5
result = add_5(3)  # Calls the inner function with y = 3
print(result)  # Output: 8


"""

# 4:- What is the purpose of the `return` statement in a Python function?
"""
Sol :- he return statement in Python is used to send a result or value from a function back to the caller. 
It allows the function to produce an output that can be used elsewhere in the program. 
Without a return statement, a function will return None by default.

Code : def add(a, b):
    return a + b  # Returns the sum of a and b

result = add(3, 4)  # Calls the function and stores the returned value
print(result)  # Output: 7

"""

# 5:-  What are iterators in Python and how do they differ from iterables?
"""
Sol 5:  Iterables:
An iterable is any Python object that can be iterated (looped) over, meaning that you can use it in a for loop or pass it to functions 
like list(), sum(), etc. An iterable is an object that implements the __iter__() method or the __getitem__().
Example

# A list is an iterable
numbers = [1, 2, 3, 4]

# Using an iterable in a for loop
for number in numbers:
    print(number)

    
An iterator is an object that actually performs the iteration. 
It keeps track of the current state of the iteration and knows how to access the next item in the sequence. 
An iterator must implement two methods:

Example :- 
# Creating an iterator from an iterable (list)
numbers = [1, 2, 3, 4]
iterator = iter(numbers)  # 'numbers' is an iterable

# Manually iterating using the iterator
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
# next(iterator) would now raise StopIteration because no elements are left



"""

# 6 :  Explain the concept of generators in Python and how they are defined?
"""
Sol  A generator in Python is a special type of iterable, like a list or a tuple, but unlike lists, 
they don’t store their elements in memory. Instead, they generate the elements one at a time using a lazy evaluation approach
meaning values are produced only when required 
This makes generators more memory efficient for working with large datasets or infinite sequences
 Using the yield Keyword
yield produces a value and suspends the functions execution. The function can later be resumed from where it left off 
which allows generators to produce values lazily
Each time the generator is called, it resumes execution from the last yield statement
Example:--
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
    
"""

# 7 What are the advantages of using generators over regular functions?
"""
Sol :- Some tasks that involve iteration over large data structures or streams can result in complex and lengthy code
In such cases, using generators can simplify the code by encapsulating the logic of iteration within the generator itself
Generators allow you to encapsulate iteration logic inside a simple function using yield, 
which simplifies the code and makes it more readable compared to manually managing iteration with while loops or maintaining states in regular functions
Example :-

# Regular function using a while loop
def get_even_numbers(n):
    numbers = []
    i = 0
    while i < n:
        if i % 2 == 0:
            numbers.append(i)
        i += 1
    return numbers

# Generator function using yield
def generate_even_numbers(n):
    i = 0
    while i < n:
        if i % 2 == 0:
            yield i
        i += 1

# Using regular function
evens = get_even_numbers(10)

# Using generator
gen_evens = generate_even_numbers(10)

"""

# 8:-  What is a lambda function in Python and when is it typically used?
"""
Sol :- A lambda function in Python is a small, anonymous function defined using the lambda keyword. 
Unlike regular functions that are defined using the def keyword and have a name, 
a lambda function is typically used for short, simple operations that are not intended to be reused elsewhere

Example of a Lambda Function:
# A lambda function that adds two numbers
add = lambda x, y: x + y

# Calling the lambda function
result = add(3, 5)
print(result)  # Output: 8

"""
#9  Explain the purpose and usage of the `map()` function in Python?
"""
Sol- The map() function in Python is a built-in function that allows you to apply a given function to all items in an iterable 
(such as a list, tuple, or set) and return a map object (which is an iterator) that produces the results. 
The key idea is to transform each element of an iterable using a function and get a new iterable of the transformed elements
Example of map()
# A simple function to square a number
def square(x):
    return x * x

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Apply the square function to each element in the numbers list using map
squared_numbers = map(square, numbers)

# Convert the map object to a list and print the result
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


"""

# 10 :- . What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?
"""
Sol:- map() Function
Purpose: The map() function is used to apply a given function to every item in an iterable 
and return a new iterator with the results of applying the function
Output: It returns an iterator that produces the results of applying the function to each item
Example :- 
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]


    filter() Function
Purpose: The filter() function is used to apply a given function to 
each item in an iterable and return a new iterator containing only those elements for which the function returns True
Output: It returns an iterator that yields the elements for which the function returned True.
Example :- 

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]


     reduce() Function
Purpose: The reduce() function is used to apply a given binary function 
(i.e., a function that takes two arguments) cumulatively to the items of an iterable, reducing the iterable to a single value.
Output: It returns a single value (not an iterator) that is the cumulative result of applying the function.

Example : -
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24

"""
