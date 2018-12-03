filename = "input_data/dec3.txt"

#list of all the id's
ids = []

#Store all the taken squares
filled_spots = {} #key:tuple value:list

#Read in the data
f = open(filename)
for line in f:
    line = line.rstrip('\n')
    #parse the input
    id_val = int(line[1:line.find('@')-1])
    left_start = int(line[line.find('@')+2:line.find(',')])
    top_start = int(line[line.find(',')+1:line.find(':')])
    width = int(line[line.find(':')+2:line.find('x')])
    height = int(line[line.find('x')+1:])
    #Add the id to the list of ids
    ids.append(0)
    #Go through and fill in all the squares it occupies
    for i in range(width):
        for j in range(height):
            square = (left_start+i,top_start+j) #make the key for the dict
            if(square in filled_spots):
                filled_spots[square].append(id_val)
                for k in filled_spots[square]:
                    ids[k-1] = 1
            filled_spots[square] = []
            filled_spots[square].append(id_val)

f.close()
not_doubled = 0
for i in range(len(ids)):
    if(ids[i]==0):
        not_doubled = i+1

print(not_doubled)
