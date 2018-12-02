from numpy import loadtxt

#Load data
filename = "input_data/dec1.txt"
#filename = "/home/debbie/Downloads/day1.txt"
changes = loadtxt(filename)

#Dict of all the sums
sums = {}

#Tracking the sum and whether or not we've found a repeat
total = 0
repeated = False

#Storing the final answer
answer = 0

#Keep looping until we find a repeat
while not repeated:
    for i in range(len(changes)):
        #Calculate the new sum
        total=total+int(changes[i])
        if(total in sums): #If the sum is a repeat
            answer = total
            repeated = True
            break
        else: #Otherwise add the sum to the dictionary
            sums[total] = 1

#print the solution
print(answer)
