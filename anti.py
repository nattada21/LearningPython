#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

"""
python3 anti.py
TTTTTTTTTTTCAGT
"""

anti = ''

i = len(dna)
while i > 0:
    if dna[i-1] == 'A':
        anti += 'T'
    elif dna[i-1] == 'C':
        anti += 'G'
    elif dna[i-1] == 'T':
        anti += 'A'
    elif dna[i-1] == 'G':
        anti += 'C'
    i -= 1

print(anti)
