# Author: ManuelADSantos
# Description: Solution for day 1 of the 2023 Advent of Code challenge
# Date: 13/12/2023

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_first(line):
    first_seen = ''
    # Read forward
    for char in line:
        # If the character is numeric
        if char.isnumeric():
            first_seen = char
            return str(first_seen)
        # If the character is not numeric, build the string
        else:
            first_seen += char
            for digit in digits:
                # If the string contains a digit
                if digit in first_seen:
                    return str(digits.index(digit) + 1)
                    
def get_last(line):
    last_seen = ''
    # Read backward
    for char in line[::-1]:
        # If the character is numeric, we have found the first number
        if char.isnumeric():
            last_seen = char
            return str(last_seen)
        # If the character is not numeric, build the string
        else:
            last_seen += char
            for digit in digits:
                # If the string inversed contains a digit
                if digit in last_seen[::-1]:
                    return str(digits.index(digit) + 1)



if __name__ == '__main__':
    # ===== Open file
    file = open('real_2.txt', 'r')
    
    # ===== Read Lines
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    file.close()

    # ===== Initialize sum
    sum = 0

    # ===== Iterate over lines
    # count = 0
    for line in lines:
        # print("-> Line " + str(count) + ": " + get_first(line) + " " + get_last(line))
        # count += 1
        sum += int(get_first(line))*10 + int(get_last(line))

    # ===== Show result
    print("The result is " + str(sum))