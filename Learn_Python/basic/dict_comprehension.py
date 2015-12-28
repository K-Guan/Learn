#!/usr/bin/env python3
"""
A demo of Python dict comprehension from a tutorial.
Check the output and the comments to learn the dict comprehension.
"""

# create a demo list
my_phrase = ["No", "one", "expects", "the", "Spanish", "Inquisition"]

"""
Use dict comprehension to create a dict, check the output
to understand how does it work.

AND I KNOW THAT THIS CAN ALSO BE DONE VIA THE FOLLOWING CODE WITHOUT DICT
COMPREHENSION: `dict(reversed(i) for i in enumerate(my_phrase))`
"""
my_dict = {key: value for value, key in enumerate(my_phrase)}
print(my_dict)

# use dict comprehension reverse the dict as `value: key`
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)
