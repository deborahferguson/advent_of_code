filename = "input_data/dec2.txt"

#open file
f = open(filename)

#Store all the previous ids
ids = []

#Set initial answer to nothing
answer = ""

#Set a found variable so you don't keep searching
found = False

#For each new id
for line in f:
    #Get rid of new line character
    line = line.rstrip('\n')
    #For each possible mismatched index
    for i in range(len(line)):
        #Get rid of that index
        cropped_line = line[:i]+line[i+1:]
        #Compare to each previous id
        for val in ids:
            #Get rid of the mismatched index for the id you're comparing too
            cropped_val = val[:i]+val[i+1:]
            #If they match you found your answer
            if(cropped_line == cropped_val):
                answer = cropped_line
                found = True
                break
        if(found):
            break
    if(found):
        break
    #Add the new id to your list
    ids.append(line)

#Print the answer
print(answer)
