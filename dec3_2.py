filename = "input_data/dec3.txt"

#list of all the id's
ids = []

#Store all the taken squares
filled_spots = {} #key:tuple value:list

#Read in the data
f = open(filename)
for line in f:
    line = line.rstrip('\n')
    #Store index locations
    ind_at = line.find('@')
    ind_comma = line.find(',')
    ind_colon = line.find(':')
    ind_x = line.find('x')
    #parse the input
    id_val = int(line[1:ind_at-1])
    left_start = int(line[ind_at+2:ind_comma])
    top_start = int(line[ind_comma+1:ind_colon])
    width = int(line[ind_colon+2:ind_x])
    height = int(line[ind_x+1:])
    #Add the id to the list of ids
    ids.append(0)
    #Go through and fill in all the squares it occupies
    for i in range(width):
        for j in range(height):
            square = (left_start+i,top_start+j) #make the key for the dict
            if(square in filled_spots):#if it exists, add the index to it
                filled_spots[square].append(id_val)
                for k in filled_spots[square]:
                    ids[k-1] = 1
            else: #otherwise make a set for it
                filled_spots[square] = [id_val]

f.close()
not_doubled = 0
for i in range(len(ids)):
    if(ids[i]==0):
        print(i+1)
        break
