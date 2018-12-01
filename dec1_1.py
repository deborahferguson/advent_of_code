import numpy as np

filename = "input_data/dec1_1_2.txt"

changes = np.loadtxt(filename)

resulting_frequency = np.sum(changes)

print(int(resulting_frequency))
