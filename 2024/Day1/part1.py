# Author: ManuelADSantos
# Description: Solution for day 1 of the 2024 Advent of Code challenge
# Date: 11/12/2024

# ===== Open file
# file = open('part1_fake.aoc', 'r')
file = open('part1_input.aoc', 'r')

# ===== Read Lines
Lines = file.readlines()
file.close()

# ===== Initialize result
result = 0

# ===== Initialize lists
list1 = []
list2 = []

# ===== Iterate over lines
for line in Lines:
    # ===== Get line
    line = line.strip('\n')
    line = line.split(' ')
    
    # ===== Save numbers in lists
    list1.append(int(line[0]))
    list2.append(int(line[-1]))

# ===== Order lists
list1.sort()
list2.sort()

# ===== Calculate distances
for i in range(len(list1)):
    result += abs(list1[i] - list2[i])

# ===== Show result
print("The result is " + str(result))