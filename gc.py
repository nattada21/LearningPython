#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change


"""
python3 gc.py
0.42
0.42
0.42
"""

gc = 0

for i in range(len(dna)):
    if dna[i] == 'G' or dna[i] == 'C':
        gc += 1

print(gc/len(dna))
