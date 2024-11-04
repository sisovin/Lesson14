# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:36:55 2024

@author: chien
"""
# %%
from math import pi
import sys
import random as rdm # alias
from turtle import title
from enum import Enum
import kansas
from game_rps import rock_paper_scissors

print("")
title = " Lesson 14: Modules inside Modules "
print(f"{title}".upper().center(80, "="))
print("")

title = " # Part of Math module with function(Pi) # "
print(f"{title}".center(80, "_"))
# Part of Math module with function(Pi)

print(pi) # Output: 3.141592653589793 // direct access to the function
print("")

title = " # Part of Random module with function(rdm) # "
print(f"{title}".center(80, "_"))
# Part of Random module with function(rdm)

for item in dir(rdm): # Output: choice, randrange, randint, etc. // access to the function through alias
    print(item) # Output: choice, randrange, randint, etc.

print("")

title = " # Part of Kansas module ) # "
print(f"{title}".center(80, "_"))
# Part of Kansas module

print(kansas.capital) # Output: Topeka // direct access to the function
kansas.randomfunfact() # Output: random fun fact // access to the function through module

print(__name__) # Output: __main__ // access to the function through module
print(kansas.__name__) # Output: kansas // access to the function through module

rock_paper_scissors() # Output: play_rps // access to the function through module
# %%
