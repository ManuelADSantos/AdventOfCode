# Author: ManuelADSantos
# Description: Solution for day 4 of the 2024 Advent of Code challenge
# Date: 11/12/2024

# ===== Open file
file = open('train.aoc', 'r')
# file = open('input.aoc', 'r')

# ===== Read Lines
Lines = file.readlines()
file.close()

# ===== Initialize result
result = 0

data = [[""] * len(Lines[0])] * len(Lines)

print(data)

# ===== Iterate over lines
for i in range(len(Lines[0])):
    for j in range(len(Lines)):
        data[i][j] = Lines[i][j]
    


# ===== Show result
print("The result is " + str(result))