"""Tidy up this file.

This file runs, but it's a mess!
Go through it and change it until there are no more linter errors or warnings.
Make sure that your code still runs without any errors by pressing
[ctrl]+[shift]+[b] as often as you think you need to.
"""
from __future__ import division
from __future__ import print_function
import os


jobs = ['get', 'this', 'file', 'to', 'pass', 'the', 'linter']
InOtherWords = "make it show no linter errors"

print ("hello! Let's get started")
print(jobs)
print(InOtherWords)
print(2, "is smaller than", 7*0.5, "is", (2) < (7*0.5), ", which is a relief!")


def usefulFunction():
    """Function."""
    print(os.getcwd())


usefulFunction()
