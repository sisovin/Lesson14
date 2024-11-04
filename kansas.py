# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%

from random import choice
from turtle import title

print("")
title = " Lesson 14: Modules "
print(f"{title}".upper().center(80, "="))
print("")

title = " # The largest city is Wichita, but Kansas City was guessed. # "
print(f"{title}".center(80, "_"))
# The largest city in Kansas is Wichita, but Kansas City was guessed.

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"

def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]
    
    index = choice("0123")
    
    print(funfacts[int(index)])
    
if __name__ == "__main__":
    randomfunfact()


