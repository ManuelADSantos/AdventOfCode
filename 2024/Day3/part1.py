# Author: ManuelADSantos
# Description: Solution for day 3 of the 2024 Advent of Code challenge
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
    # Seperate line by 'mul'
    line = line.split('mul')
    
    # For each section
    for sub in line:
        # If after 'mul' does not come a '('
        if sub[0]!='(':
            continue
        
        # If there's not at leat 1 '(', ')' or ','
        if sub.count('(')<1 or sub.count(')')<1 or sub.count(',')<1:
            continue
        
        # Get only content between '(' to ',' and ',' to ')'
        sub = sub[1:sub.find(')')]
        sub = sub.split(',')
        
        # If there's more than 2 'numbers'
        if len(sub)!=2:
            continue  
        
        # Make sure they are 'numbers'
        if not sub[0].isnumeric() or not sub[1].isnumeric():
            continue
        
        # Multiply them
        result += int(sub[0])*int(sub[1])


# ===== Show result
print("The result is " + str(result))