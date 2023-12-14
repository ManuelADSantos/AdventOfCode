# Author: ManuelADSantos
# Description: Solution for day 1 of the 2023 Advent of Code challenge
# Date: 13/12/2023

# ===== Open file
file = open('real_1.txt', 'r')

# ===== Read Lines
Lines = file.readlines()
file.close()

# ===== Initialize sum
sum = 0

# ===== Iterate over lines
for line in Lines:
    # ===== Get line
    # print(line.strip())
    line = line.strip()
    
    # ===== Get first and last number
    first = True
    first_seen = ''
    last_seen = ''
    for char in line:
        if char.isnumeric():
            if first:
                first_seen = char
                last_seen = char
                first = False
            else:
                last_seen = char

    # ===== Show first and last number
    # print("First: " + first_seen + " | Last: " + last_seen)

    # ===== Add result to sum
    sum += 10*int(first_seen) + int(last_seen)   

# ===== Show result
print("The result is " + str(sum))