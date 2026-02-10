# Assignment 2 Question 3
# Joseph Krosel

# Imports library
from collections import Counter
import string

# Reads the file line by line
with open("sample-file.txt", 'r') as file:
    lines = file.readlines()

normalized_dict = {}

for line_number, line in enumerate(lines, start=1):
    original_line = line.rstrip('\n')

    # Normalize: lowercase, remove whitespace & punctuation
    normalized = ""
    for ch in original_line.lower():
        if ch.isalpha():
            normalized += ch

    # ignore empty normalized lines
    if normalized == "":
        continue

    if normalized not in normalized_dict:
        normalized_dict[normalized] = []
    normalized_dict[normalized].append((line_number, original_line))

# Keep only sets with duplicates
duplicate_sets = [
    group for group in normalized_dict.values()
    if len(group) > 1
]

print(f"Number of sets with duplicates: {len(duplicate_sets)}")

# Print first two sets
for i, group in enumerate(duplicate_sets[:2], start=1):
    print(f"\nSet {i}:")
    for line_number, text in group:
        print(f"  Line {line_number}: {text}")