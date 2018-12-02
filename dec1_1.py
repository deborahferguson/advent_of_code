import numpy as np

#Load the data
filename = "input_data/dec1.txt"
changes = np.loadtxt(filename)

#Sum all the changes
resulting_frequency = np.sum(changes)

#Output the solution as an int
print(int(resulting_frequency))
