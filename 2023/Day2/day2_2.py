# Author: ManuelADSantos
# Description: Solution for day 2 of the 2023 Advent of Code challenge
# Date: 14/12/2023

# =============== Function to check if game is valid ===============
def get_cubes_game(line):
    # ===== Split line
    sets = line[7::].split(';')

    # ===== Get max for each color
    max_game = {"red": 0, "green": 0, "blue": 0}

    for set in sets:
        max_set = get_max_set(set)

        if(max_set["red"] > max_game["red"]):
            max_game["red"] = max_set["red"]
        
        if(max_set["green"] > max_game["green"]):
            max_game["green"] = max_set["green"]
        
        if(max_set["blue"] > max_game["blue"]):
            max_game["blue"] = max_set["blue"]
        
    return max_game

def get_max_set(set):
    # ===== Split set
    draws = set.split(',')

    # ===== Initialize max
    max = {"red": 0, "green": 0, "blue": 0}

    # ===== Get max for each color
    for draw in draws:
        if("red" in draw):
            draw = draw.split(' ')
            if(int(draw[1]) > max["red"]):
                max["red"] = int(draw[1])

        if("green" in draw):
            draw = draw.split(' ')
            if(int(draw[1]) > max["green"]):
                max["green"] = int(draw[1])
            
        if("blue" in draw):
            draw = draw.split(' ')
            if(int(draw[1]) > max["blue"]):
                max["blue"] = int(draw[1])

    return max


# =============== Main Execution ===============
if __name__ == '__main__':
    # ===== Open file
    file = open('real_2.txt', 'r')

    # ===== Read Lines
    Lines = file.readlines()
    Lines = [line.strip() for line in Lines]
    file.close()

    # ===== Initialize sum
    sum = 0

    for line in Lines:
        # print(line)
        cubes = get_cubes_game(line)
        sum += cubes["red"] * cubes["green"] * cubes["blue"]

    # ===== Show result
    print("The result is " + str(sum))# Author: ManuelADSantos
