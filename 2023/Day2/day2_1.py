# Author: ManuelADSantos
# Description: Solution for day 2 of the 2023 Advent of Code challenge
# Date: 14/12/2023

# =============== Function to check if game is valid ===============
def is_game_valid(line):
    # ===== Split line
    sets = line[7::].split(';')
    for set in sets:
        if(is_set_valid(set)):
            continue
        else:
            return False
        
    return True

def is_set_valid(set):
    # ===== Split set
    draws = set.split(',')
    for draw in draws:
        if("red" in draw):
            draw = draw.split(' ')
            if(int(draw[1]) > 12):
                return False

        if("green" in draw):
            draw = draw.split(' ')
            if(int(draw[1]) > 13):
                return False
            
        if("blue" in draw):
            draw = draw.split(' ')
            if(int(draw[1]) > 14):
                return False

    return True


# =============== Main Execution ===============
if __name__ == '__main__':
    # ===== Open file
    file = open('real_1.txt', 'r')

    # ===== Read Lines
    Lines = file.readlines()
    Lines = [line.strip() for line in Lines]
    file.close()

    # ===== Initialize sum
    sum = 0
    count = 1

    for line in Lines:
        # print(line)
        if(is_game_valid(line)):
            print("Game " + str(count) + " is valid")
            sum += count
        count += 1

    # ===== Show result
    print("The result is " + str(sum))