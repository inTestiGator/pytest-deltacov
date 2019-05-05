import csv
import pandas as pd

deltas = []

with open('deltacov.csv', 'r', newline='') as f:
    lines = f.readlines()
    if len(lines) < 10:
        for i in range(len(lines)):
            print(lines[i])
            #delta = lines[i+1][1] - lines[i][1]
            #deltas.append(delta)

    else:
        start_position = len(lines) - 10
        last_10 = lines[start_position:]
        for i in range(len(last_10)-1):
            delta = last_10[i+1][1] - last_10[i][1]
            deltas.append(delta)

print(deltas)
