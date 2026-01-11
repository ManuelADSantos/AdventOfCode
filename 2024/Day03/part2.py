# Author: ManuelADSantos
# Description: Solution for day 3 of the 2024 Advent of Code challenge
# Date: 13/12/2024

# ===== Open file
# file = open('part2_train.aoc', 'r')
file = open('input.aoc', 'r')

# ===== Read Lines
Lines = file.readlines()
file.close()

# ===== Initialize result
result = 0

to_do = True

# ===== Iterate over lines
for line in Lines:
    # Seperate line by 'mul'
    line = line.split('mul')
    
    # For each section
    for sub in line:
        has_number = True
        original_sub  = sub
        print(f":: {sub} | to_do:{to_do}")
        
        if len(sub) == 1:
            continue
        
        # If after 'mul' does not come a '('
        if sub[0]!='(':
            # continue
            has_number = False
        
        # If there's not at leat 1 '(', ')' or ','
        if sub.count('(')<1 or sub.count(')')<1 or sub.count(',')<1:
            # continue
            has_number = False
        
        # Get only content between '(' to ',' and ',' to ')'
        if has_number:
            sub = sub[1:sub.find(')')]
            sub = sub.split(',')
        
        # If there's more than 2 'numbers'
        if has_number and len(sub)!=2:
            # continue
            has_number = False 
        
        # Make sure they are 'numbers'
        # print(f"sub:{sub}")
        if has_number:
            if not sub[0].isnumeric() or not sub[1].isnumeric():
                # continue
                has_number= False
        
        # Multiply them
        if to_do and has_number:
            print(f"(+) Add mul({int(sub[0])},{int(sub[1])})")
            result += int(sub[0])*int(sub[1])
        elif not to_do and has_number:
            print(f"(-) Don't add mul({int(sub[0])},{int(sub[1])})")
            
        if "do()" in original_sub:
            print(f"(V) Activate")
            to_do = True
        
        if "don't()" in original_sub:
            print(f"(X) Deactivate")
            to_do = False

# ===== Show result
print("===> The result is " + str(result))