# Author: ManuelADSantos
# Description: Solution for day 2 of the 2024 Advent of Code challenge
# Date: 12/12/2024

# ===== Open file
# file = open('train.aoc', 'r')
file = open('input.aoc', 'r')

# ===== Read Lines
Lines = file.readlines()
file.close()

# ===== Initialize result and total
result = 0
total = 0
deep = 0

def is_it_safe(report: list, layer: bool)->bool:
    print(f"(R) report {report}")
    for i in range(len(report)-1):
        level_x = report[i]
        level_y = report[i+1]
        print(f"level_x:{level_x}|level_y:{level_y} ({level_y-level_x})")

        # If difference smaller than 1 or bigger than 3
        if level_y-level_x<1 or level_y-level_x>3:
            print("(X) Nope")
            global deep
            deep += 1
            
            if deep >= 2:
                print("*** BOOM ***")
                return False
            else:
                return is_it_safe(report[:i] + report[i + 1:], deep) or is_it_safe(report[:i + 1] + report[i + 2:], deep)
    
    print(f"(V) Report all good {report}")
    return True

# ===== Iterate over lines
for line in Lines:
    
    total += 1
    # Get line
    line = line.strip('\n')
    line = line.split(' ')
    line = [int(x) for x in line]

    # Make sure every line is ascending
    if line[0] > line[-1]:
        line.reverse()

    deep = 0
    safe = is_it_safe(report = line, layer = deep)

    if safe:
        result += 1

    print(" ")
    # input("===================================\n")

# ===== Show result
print(f"The result is {result} SAFE out of {total}")