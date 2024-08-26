

'''
Q 1) What is the difference between a function and a method in Python?

Ans) The function is a self bound it is not bound by the other objects whereas the method is bound to the objects.
method is bound with thw class or object
let see the example of both
'''

def add(a,b):  # this is function
    return a+b

class Calc:   # this is class
  def __init__(self,a,b):   # this is method and this is bound with calc class
    self.a=a
    self.b=b
  def sub(self):
    return self.a-self.b
print(add(2,3))   # we can call function directly
c=Calc(3,2)    # for method calling we have to create instance of the class
c.sub()    # calling method through the class object
     


'''
Q  2. Explain the concept of function arguments and parameters in Python.

Ans) When we are making funcyion at that we have to set the how many  parameter we  want in the function according to that we have to
give the value, while in the arguments while we are calling the function we have to put the arguments to pass in the parameter
'''

def greet(name):  # this is parameter in the function
  print(f"Hello {name}")

greet("Amarjeet Choudhary")

     


'''
Q 3) What are the different ways to define and call a function in Python?

Ans) There are many ways to call and define the function
lets discuss through the programming
'''

#method 1

def  func_method_1():
  pass

#method 2 we can make nested funnction
def outer():
  def inner():
    pass

# method 3 lambda function

double = lambda x: x * 2

print(double(5))

#Methods of calling

#1
func_method_1()  #simple way

#2
 #map(function_name, iterable)  # using map

#3
#filter(function_name, iterable)  # using filter

#4
#reduce(function_name, iterable)  # using reduce

     


'''
Q 4) What is the purpose of the `return` statement in a Python function?

Ans) The purpose of the return statement is to return the value from the function. It is used to end the execution of the function and return
 the result to the caller. by using return we can store that value outside the function
'''
     

'''
Q 5) What are iterators in Python and how do they differ from iterables?

Ans) The key difference between the two is that iterables can be iterated over multiple times, while iterators can only be used once.
When you exhaust an iterator, you need to create a new one to iterate again. Iterables, however, can be iterated over repeatedly without
needing to create a new object. For example, you can iterate over a list multiple times using a for loop, but if you use the iter() function
to create an iterator object, it can only be iterated over once.
'''

my_list = [1, 2, 3]  # iterable
my_iter = iter(my_list)  # iterator

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
     


'''
Q 6) Explain the concept of generators in Python and how they are defined.

Ans)Generators in Python are a type of iterable, like lists or tuples, but unlike those, generators do not store all of their values in memory.
 Instead, they generate values on the fly and can be iterated through one value at a time, which makes them more memory-efficient for handling
 large datasets.
'''
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

seq = infinite_sequence()
for _ in range(10):
    print(next(seq))
     


'''
Q 7) What are the advantages of using generators over regular functions?

Ans) The generatres are the memeory effiecient it stores the one value at the time .Even generatores can handle the large dataset
Generatore simplyfying the code perfomance and memory usage.
'''
     

'''
Q 8)  What is a lambda function in Python and when is it typically used?

Ans) A lambda function is a small, anonymous function in Python that can take any number of arguments, but can only have one expression.
 It's a shorthand way to define a simple function without declaring a named function. Lambda function makes coding more precise ,no noeed to
 declare the name
'''

double = lambda x: x * 2

print(double(5))
     


'''
Q 9) Explain the purpose and usage of the `map()` function in Python.

Ans) The map() function applies a given function to each item of an iterable, such as a list, tuple, or string, and returns a list of the
results. This function is useful for data transformation, concise code, and functional programming techniques. It takes two arguments: the
function to apply and the iterable to apply it to.

'''

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
     


'''
Q 10) What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?

Ans) The map() function applies a given function to each item of an iterable, such as a list, tuple, or string, and returns a list of the
results. This function is useful for data transformation, concise code, and functional programming techniques.
The reduce() Applies a function to the first two items in an iterable, then to the result and the next item, and so on, return a
 single output values
The filter() Applies a function to each item in an iterable and returns only the items for which the function returns True,returns a new iterable
 with the filtered items, the main purpose of Data filtering, selection
'''

from functools import reduce

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
     
