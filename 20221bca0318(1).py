# -*- coding: utf-8 -*-
"""20221BCA0318(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EhESrY_5v_e83vyW3hk-BT_4_w9tbVYy

*Functional Programming*

Functional programming decomposes a problem into a set of functions.
Ideally, functions only take inputs and produce outputs, and don’t have any internal state that affects the output produced for a given input.

Well-known functional languages include the ML family (Standard ML, OCaml, and other variants) and Haskell

Functional programming offers various features such as ***iterators and generators*** and relevant library modules such as ***itertools and functools***.

Functional programming can be considered the opposite of ***object-oriented programming***.

Objects are little capsules containing some internal state along with a collection of method calls that let you modify this state, and programs consist of making the right set of state changes.

Functional programming wants to avoid state changes as much as possible and works with data flowing between functions.

In Python you might combine the two approaches by writing functions that take and return instances representing objects in your application (e-mail messages, transactions, etc.)

There are theoretical and practical advantages to the functional style:

•	Formal provability.

•	Modularity.

•	Composability.

•	Ease of debugging and testing

## ***Iterators***
A Python language feature that’s an important foundation for writing functional-style programs: iterators.

An iterator is an object representing a stream of data; this object returns the data one element at a time.

A Python iterator must support a method called __next__() that takes no arguments and always returns the next element of the stream.

If there are no more elements in the stream, __next__() must raise the StopIteration exception.

Iterators don’t have to be finite, though; it’s perfectly reasonable to write an iterator that produces an infinite stream of data.

The built-in iter() function takes an arbitrary object and tries to return an iterator that will return the object’s contents or elements, raising TypeError if the object doesn’t support iteration.

Several of Python’s built-in data types support iteration, the most common being lists and dictionaries.

**An object is called iterable if you can get an iterator for it.**
"""

L = [10,12,15,17]
it = iter(L)
it

next(it)

it.__next__()

next(it)

next(it)

for i in iter(L):
  print(i)

for i in L:
  print(i)

"""# ***Iterators can be materialized as lists or tuples by using the list() or tuple() constructor functions:***"""

L = [10,12,15,17]
iterator = iter(L)
t = tuple(iterator)
t

"""# ***Sequence unpacking also supports iterators: if you know an iterator will return N elements, you can unpack them into an N-tuple***"""

L = [10,12]
iterator = iter(L)
a, b = iterator
a, b

"""Built-in functions such as max() and min() can take a single iterator argument and will return the largest or smallest element.

The "in" and "not in" operators also support iterators: X in iterator is true if X is found in the stream returned by the iterator.


Note that you can only go forward in an iterator; there’s no way to get the previous element, reset the iterator, or make a copy of it. Iterator objects can optionally provide these additional capabilities, but the iterator protocol only specifies the __next__() method. Functions may therefore consume all of the iterator’s output, and if you need to do something different with the same stream, you’ll have to create a new iterator.

# ***Data Types That Support Iterators***


Calling iter() on a dictionary returns an iterator that will loop over the dictionary’s keys:
"""

m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
for key in m:
  print(key, m[key])

"""# Applying ***iter()*** to a dictionary always loops over the keys, but dictionaries have methods that return other iterators. If you want to iterate over values or key/value pairs, you can explicitly call the values() or items() methods to get an appropriate iterator.
# The ***dict()*** constructor can accept an iterator that returns a finite stream of (key, value) tuples:

"""

l=[4,2,8]
[2*i for i in l]

l=[12,16,14]
for i in l:
  x=2*i
  print(x)

[2*i for i in l]

L = [('France', 'Paris'), ('US', 'Washington DC')]
dict(iter(L))

"""**List comprehensions** and **generator expressions** (short form: *“listcomps”* and *“genexps”*) are a concise notation for such operations, borrowed from the functional programming language Haskell (https://www.haskell.org/). You can strip all the whitespace from a stream of strings with the following code:"""

line_list = ['  Gitam University\n', ' School of information science\n', ' BCA \n', '  \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
print(stripped_list)

#You can select only certain elements by adding an "if" condition:
stripped_list = [line.strip() for line in line_list if line != " "]
print(stripped_list)

"""## ***Generators***
With a list comprehension, you get back a Python list; stripped_list is a list containing the resulting lines, not an iterator.

Generator expressions return an iterator that computes the values as necessary, not needing to materialize all the values at once. This means that list comprehensions aren’t useful if you’re working with iterators that return an infinite stream or a very large amount of data.

Generator expressions are preferable in these situations.

Generator expressions are surrounded by parentheses (“()”) and list comprehensions are surrounded by square brackets (“[]”).

Generator expressions have the form:

( expression for expr in sequence1
             
             if condition1
             for expr2 in sequence2
             if condition2
             for expr3 in sequence3
             ...
             if condition3
             for exprN in sequenceN
             if conditionN )
Again, for a list comprehension only the outside brackets are different (square brackets instead of parentheses).
The elements of the generated output will be the successive values of expression. The if clauses are all optional; if present, expression is only evaluated and added to the result when condition is true.
Generator expressions always have to be written inside parentheses, but the parentheses signalling a function call also count. If you want to create an iterator that will be immediately passed to a function you can write:

obj_total = sum(obj.count for obj in list_all_objects())

The for...in clauses contain the sequences to be iterated over. The sequences do not have to be the same length, because they are iterated over from left to right, not in parallel. For each element in sequence1, sequence2 is looped over from the beginning. sequence3 is then looped over for each resulting pair of elements from sequence1 and sequence2.
To put it another way, a list comprehension or generator expression is equivalent to the following Python code:

for expr1 in sequence1:
    
    if not (condition1):
        continue   # Skip this element
    for expr2 in sequence2:
        if not (condition2):
            continue   # Skip this element
        ...
    for exprN in sequenceN:
            if not (conditionN):
                continue   # Skip this element

            # Output the value of
            # the expression.
This means that when there are multiple for...in clauses but no if clauses, the length of the resulting output will be equal to the product of the lengths of all the sequences. If you have two lists of length 3, the output list is 9 elements long:
"""

seq1 = 'xyz'
seq2 = (17,19,21)
[(x, y) for x in seq1 for y in seq2]

"""### **Generators**

Generators are a special class of functions that simplify the task of writing iterators. Regular functions compute a value and return it, but generators return an iterator that returns a stream of values.

Here’s the simplest example of a generator function:

  
    def generate_ints(N):
      for i in range(N):
        yield i

Any function containing a ***yield*** keyword is a generator function;

this is detected by Python’s bytecode compiler which compiles the function specially as a result.

When you call a generator function, it doesn’t return a single value; instead it returns a generator object that supports the iterator protocol.

On executing the yield expression, the generator outputs the value of i, similar to a return statement.

The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved.

On the next call to the generator’s __next__() method, the function will resume executing.

## ***Usage of the generate_ints() generator:***
"""

def generate_ints(N):
  for i in range(N):
    yield i


gen=generate_ints(19)
next(gen)

next(gen)

send(5)

next(gen)

next(gen)

next(gen)

next(gen)

next(gen)

"""Values are sent into a generator by calling its ***send(value***) method. This method resumes the generator’s code and the yield expression returns the specified value. If the regular __next__() method is called, the yield returns None"""

def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1



it = counter(10)
next(it)

next(it)

next(it)

next(it)

it.send(8)

next(it)

next(it)

next(it)

it.send(8)

next(it)

"""In addition to ***send()***, there are two other methods on generators:

•	***throw(value)*** is used to raise an exception inside the generator; the exception is raised by the yield expression where the generator’s execution is paused.

•	***close()*** raises a GeneratorExit exception inside the generator to terminate the iteration. On receiving this exception, the generator’s code must either raise GeneratorExit or StopIteration; catching the exception and doing anything else is illegal and will trigger a RuntimeError. close() will also be called by Python’s garbage collector when the generator is garbage-collected.

Two of Python’s built-in functions, ***map()*** and ***filter()*** duplicate the features of generator expressions:

***map(f, iterA, iterB, ...) ***returns an iterator over the sequence
"""

def upper(s):
  return s.upper()

list(map(upper, ['rithika', 'reena']))

[upper(s) for s in ['rithika', 'reena']]

"""***filter(predicate, iter)*** returns an iterator over all the sequence elements that meet a certain condition, and is similarly duplicated by list comprehensions. A predicate is a function that returns the truth value of some condition;

for use with ***filter()***, the predicate must take a single value.
"""

def is_even(x):
  return (x % 2) == 0
list(filter(is_even, range(20)))

#List Comprehension
list(x for x in range(30) if is_even(x))

"""***enumerate(iter, start=0)*** counts off the elements in the iterable returning 2-tuples containing the count (from start) and each element."""

for item in enumerate(['P', 'R', 'R']):
  print(item)

"""***sort() method***"""

import random
# Generate 8 random numbers between [0, 10000)
rand_list = random.sample(range(10000), 4)
rand_list

sorted(rand_list)

sorted(rand_list, reverse=True)

"""# ***any(iter) and all(iter) built-ins***

The ***any(iter) and all(iter)*** built-ins look at the truth values of an iterable’s contents. any() returns True if any element in the iterable is a true value, and all() returns True if all of the elements are true values:
"""

any([1, 1, 3])

all([-1, 1, 0])

"""# ***zip(iterA, iterB, ...) takes one element from each iterable and returns them in a tuple:***"""

zip(['r','r','r'], (1, 2, 3))

zip(['p', 'b'], (1, 2, 4))