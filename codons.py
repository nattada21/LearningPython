#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

# your code goes here

"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""

for i in range(len(dna)):
    if i % 3 == 0:
        print(dna[i:i+3])
