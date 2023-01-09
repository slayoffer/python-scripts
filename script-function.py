#!/usr/bin/env python

def my_function():
    """This is a doc string"""
    mynum1 = 10
    mynum2 = 30
    print(mynum1 + mynum2)
    global message
    message = "Hello World!"
    print(message)

my_function()

print(message)