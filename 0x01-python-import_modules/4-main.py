#!/usr/bin/python3
raise_exception = __import__('4-raise_exception').raise_exception

try:
    raise-exception()
except TypeError as te:
    print("Exception raised")
