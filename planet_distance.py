import sys
import os
import math
import re
from collections import defaultdict

def find_cycle(universe, start=1, prev=0, cycle=[]):
    if start != prev:
        if start not in cycle:
            cycle.append(start)
        else:
            return cycle
    for planet in universe[start]:
        if planet != prev:
            newcycle = find_cycle(universe, planet, start, cycle)

            if newcycle: return newcycle

def find_min_dist(planet, universe, cycle):
    for tube in universe[planet]:

# read input file
input_file = sys.argv[1]

print('PLANET DISTANCE')

with open(input_file) as f:
    file_lines = f.readlines()
f.close()

numCases = int(file_lines[0])

output_file = open("output.txt", "w")

vals_regex = re.compile(r"(\d+) (\d+)")

#iterate through cases
currLine = 1
for caseNum in range (1, numCases+1):
    currCaseSize = int(file_lines[currLine])

    output_file.write(f'Case #{caseNum}: ')

    # setup planets graph as dict(set)
    currUniverse = defaultdict(set)

    for i in range (1, currCaseSize+1):
        currLine++
        tubedPlanets = re.search(vals_regex, file_lines[currLine]).groups()

        currUniverse[tubedPlanets[0]].append(tubedPlanets[1])
        currUniverse[tubedPlanets[1]].append(tubedPlanets[0])

    cycle = find_cycle(currUniverse)

    # write to output file
    for planet in range (1, currCaseSize+1):
        minDist = find_min_dist(planet, currUniverse, cycle)
        output_file.write(f'{minDist} ')

    output_file.write('\n')

print('\n')
print('Done! Check output.txt for results.')
