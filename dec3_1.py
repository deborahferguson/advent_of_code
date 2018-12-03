filename = "input_data/dec3.txt"

#Store all the taken squares
filled_spots = {} #key:tuble value:int

#Read in the data
f = open(filename)
for line in f:
    line = line.rstrip('\n')
    #parse the input
    left_start = int(line[line.find('@')+2:line.find(',')])
    top_start = int(line[line.find(',')+1:line.find(':')])
    width = int(line[line.find(':')+2:line.find('x')])
    height = int(line[line.find('x')+1:])
    #Go through and fill in all the squares it occupies
    for i in range(width):
        for j in range(height):
            square = (left_start+i,top_start+j) #make the key for the dict
            if(square in filled_spots):
                filled_spots[square] = filled_spots[square]+1
            else:
                filled_spots[square] = 1

f.close()
#Count up all spots with value>=2
total = 0
for key,val in filled_spots.items():
    if(val>1):
        total+=1

print(total)

