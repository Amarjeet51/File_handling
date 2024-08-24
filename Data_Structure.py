

'''
Q1) Discuss string slicing and provide examples?

Ans 1) String slicing is a technique used in programming to extract a specific portion or segment of a string. This is achieved by
specifying a range of indices that correspond to the characters you want to extract from the original string.
'''
text = "Hello, World!"
print(text[0:5])

     


'''
Q2) Explain the key features of lists in Python?

Ans 2) The features of lists are :-
1. Lists are used to store multiple items in a single variable.
2. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and
Dictionary, all with different qualities and usage.
3.Lists are mutable
4.List are dyanamically in nature
5.In list we can store heterogenous types of data
'''

     

'''
Q3) Describe how to access modify and delete elements in a list with examples?

Ans 3) We can modify and delete elements in a list like this.
'''
l = [1,2,3,4,5,6]
l.append(7)
print(l)
l.remove(1)
print(l)
del l[2]
print(l)
     


'''
Q 4) Compare and contrast tuples and lists with examples?
Ans 4) a) Tuples are immutable and list are mutable
b) In tuples we use () paranthsis and in list we use []
c) tuples generally takes less memory comapre to lists
d) Tuples are faster than lists
'''
t = (1,2,3,4,5,6)
print(t)
l = [1,2,3,4,5,6]
print(l)
     


'''
Q5) Describe the key features of sets and provide examples of their use?

Ans 5) Key features of sets are :-

a) sets are unordered collection
b)set contains only unique elements
c)Sets are mutable
d)In seta indexing and slicing is not possible
'''
s = {1,2,3,4,5,6}
s.add(7)
print(s)
s.pop()
print(s)
s.remove(2)
print(s)
     


'''
Q 6)Discuss the use cases of tuples and sets in Python programming?

Ans 6)  Tuples are immutable sequences of Python objects. They are similar to lists but cannot be changed once created.

Use Cases:

a) Representing immutable data: When you have data that should not be modified, such as coordinates (latitude, longitude), database records,
configuration settings, etc.
b) Returning multiple values from functions: Tuples are often used to return multiple values from a function.
c) As dictionary keys: Tuples can be used as dictionary keys because they are hashable, unlike lists.
d) Unpacking values: You can unpack tuples into individual variables using multiple assignment, which is often used in function return values.

'''
t = (1,2,3,'hello',4,5)
print(t)

     


'''
Q 7)  Describe how to add, modify and delete items in a dictionary with examples

Ans 7) Adding Items: Use direct assignment or update() method.
Modifying Items: Use direct assignment or update() method.
Deleting Items: Use del statement, pop() method, popitem() method, or clear() method
'''
my_dict = {"name": "Ali", "age": 29}
my_dict["city"] = "New York"
print(my_dict)
my_dict.update({"job": "Engineer"})
print(my_dict)
del my_dict["city"]
print(my_dict)

     

'''
Q 8)  Discuss the importance of dictionary keys being immitable and provide examples

Ans 8) In Python, dictionary keys must be immutable. This requirement is crucial for several reasons:

Hashing Requirement:Dictionaries use a hash table to store key-value pairs. For the hash table to work correctly, keys must be hashable, and only immutable objects
can be reliably hashed. Hashing relies on the key's value remaining constant over time, ensuring that the key can always be located within the
hash table.
Consistency and Reliability:If keys could change, the integrity of the dictionary's structure would be compromised. The hash of a mutable
object can change if its content changes, leading to unpredictable behavior when trying to retrieve or store values in the dictionary.
Performance:

Immutable keys ensure efficient lookups, insertions, and deletions. The stability provided by immutable keys allows the hash table to operate
at optimal performance without needing to constantly adjust for changes in key values.
'''
my_dict = {"name": "Ali", "age": 29}
my_dict["city"] = "New York"
print(my_dict)
my_dict.update({"job": "Engineer"})
print(my_dict)
del my_dict["city"]
print(my_dict)


     