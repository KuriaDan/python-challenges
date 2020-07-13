# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:03:19 2020

@author: Kuria
"""
"""
Challenge: write a python function to find all prime factors of a given number.
Input: integer value
Output: list of prime factors
"""
def prime_factors(N):
    divisor = 2
    factors = [] 
    while(divisor <= N):
        if (N % divisor) ==0:
            factors.append(divisor)
            N = N/divisor
        else:
            divisor+=1
    return factors
