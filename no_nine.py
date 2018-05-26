import sys
import os
import math
import re
from multiprocessing import Pool

pool = Pool()

def countNoNines( start, end ):
    nineRegex = re.compile(r"[9]")
    count = 0
    while start <= end:
        if start % 9 != 0:
            if re.search(nineRegex, str(start)) is None:
                count += 1
        start += 1
    return f'{count}'

# read input file
input_file = sys.argv[1]

print('NO NINE')

with open(input_file) as f:
    file_lines = f.readlines()
f.close()

numCases = int(file_lines[0])
tests = [None]

output_file = open("output.txt", "w")

vals_regex = re.compile(r"(\d+) (\d+)")

for i in range (1, numCases+1):
    # write to output file
    vals = re.search(vals_regex, file_lines[i]).groups()
    start = int(vals[0])
    end = int(vals[1])
    output_file.write(f'Case #{i}: ')
    output_file.write(f'{countNoNines(start, end)} ')
    output_file.write('\n')

print('\n')
print('Done! Check output.txt for results.')
