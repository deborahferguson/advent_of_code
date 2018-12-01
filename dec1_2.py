import numpy as np

filename = "input_data/dec1_1_2.txt"
changes = np.loadtxt(filename)

print(changes.shape)

sums = {}

total = 0
repeated = False

answer = 0

while not repeated:
    for i in range(len(changes)):
        total=total+int(changes[i])
        if(total in sums):
            answer = total
            repeated = True
            break
        else:
            sums[total] = 1

print(answer)
