# Author: ManuelADSantos
# Description: Helper file to save results of Advent of Code to a single .csv file
# Date: 11/12/2024

import os
import shutil
import csv

filename = "results.csv"

def save_result(result:int)->None:
    with open(csv_filename, mode='+', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        