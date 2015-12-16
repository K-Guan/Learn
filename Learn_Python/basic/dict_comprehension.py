#!/usr/bin/env python3
my_phrase = ["No", "one", "expects", "the", "Spanish", "Inquisition"]
my_dict = {key: value for value, key in enumerate(my_phrase)}
print(my_dict)

reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)
