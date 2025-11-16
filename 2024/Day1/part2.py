# Author: ManuelADSantos
# Description: Solution for day 1 of the 2024 Advent of Code challenge
# Date: 12/12/2024

# ===== Open file
# file = open('train.aoc', 'r')
file = open('input.aoc', 'r')

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


# ===== Calculate distances
for i in range(len(list1)):
    x = list1[i]
    result += x * list2.count(x)

# ===== Show result
print("The result is " + str(result))