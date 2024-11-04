# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:58:04 2024

@author: chien
"""
# %%
import mymodule
from mymodule import greet
from mymodule import my_function

print("")
print(mymodule.greet("Alice"))
print(mymodule.pi)
print("")

print(greet("Bob"))
print("")


fullname = "Chien" + " " + "Sisovin"
print(mymodule.my_function(fullname))

fullname = "Chien" + " " + "Sisovin"
print(my_function(fullname))
# %%
# Import the entire module
import mymodule

# Use the functions and variables from the module
print(mymodule.greet("Alice"))
print(mymodule.pi)

fullname = "Chien" + " " + "Sisovin"
print(mymodule.my_function(fullname))

# Import specific functions from the module
from mymodule import greet, my_function

print(greet("Bob"))
print(my_function("This is another argument."))
# %%
