import csv
import pandas as pd

with open('deltacov.csv', 'r', newline='') as f:
    lines = f.readlines()
    if len(lines) < 10:
        for line in lines:
            
    else:
        start_position = len(lines) - 10
        # print(lines[start_position:])
