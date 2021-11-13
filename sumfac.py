#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here

"""
python3 sumfac.py
5 15 120
"""

sum = 0
fact = 1
for i in range(n):
    sum += (i+1)
    fact *= (i+1)
print(n, sum, fact)
