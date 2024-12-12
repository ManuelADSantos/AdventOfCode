# Author: ManuelADSantos
# Description: Solution for day 2 of the 2024 Advent of Code challenge
# Date: 11/12/2024

# ===== Open file
# file = open('part1_fake.aoc', 'r')
file = open('part1_input.aoc', 'r')

# ===== Read Lines
Lines = file.readlines()
file.close()

# ===== Initialize result
result = 0

# ===== Iterate over lines
for line in Lines:
    # Get line
    line = line.strip('\n')
    line = line.split(' ')
    
    # Make sure every line is ascending
    if line[0]>line[-1]:
        line.reverse()
        
    # If first and last value are equal, forget it (Never happens)
    if line[0]>line[-1]:
        print("*** BOOM ***")
        continue    
    
    safe = True
    for i in range(len(line)-1):
        x = int(line[i])
        y = int(line[i+1])
        print(f"x:{x}|y:{y}")
        
        # If two equal consecutive values
        if x==y:
            safe = False
            print("*** BOOM ***")
            break
        
        # If difference smaller than 1 or bigger than 3
        if y-x<1 or y-x>3:
            safe = False
            print("*** BOOM ***")
            break
        
    if safe:
        result += 1
    
    print(" ")
    
# ===== Show result
print("The result is " + str(result))