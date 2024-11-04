# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:51:46 2024

@author: chien
"""

from turtle import title

print("")
title = " Lesson 14: Modules in mymodule.py "
print(f"{title}".upper().center(80, "="))
print("")

title = " # Creating a Module: # "
print(f"{title}".center(80, "_"))
# Creating a Module:


def greet(name):
    return f"Hello, {name}!"

pi = 3.14159

def my_function(my_variable):
    return f"My name is {my_variable}!"
