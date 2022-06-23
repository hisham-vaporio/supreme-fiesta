#!/bin/env python

def foo(a):  # NonCompliant
    b = 12
    if a == 1:
        return b
    return b

print("Hello World!")
print("Does this work?")
print(f"{foo(1)}")
