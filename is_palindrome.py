# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:41:42 2020

@author: Kuria
"""
"""
Challenge: write a python function to determine if a given string is a palindrome

input: string to evaluate
output: boolean value
constraints: only consider letters(A-Z)
           : ignore case(for example, 'A' == 'a')
"""

import re
def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards