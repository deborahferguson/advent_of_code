filename = "input_data/dec6.txt"
f = open(filename,'r')
coordinates = []
min_x = None
max_x = None
min_y = None
max_y = None
first = True
for line in f:
    values = line.split(', ')
    x = int(values[0])
    y = int(values[1])
    coordinates.append((x,y))
    if(first):
        min_x = x
        max_x = x
        min_y = y
        max_y = y
        first = False
    else:
        if(x<min_x):
            min_x = x
        if(x>max_x):
            max_x = x
        if(y<min_y):
            min_y = y
        if(y>max_y):
            max_y = y
f.close()


count = 0
#grid = []
for i in range(max_x-min_x):
    column = []
    for j in range(max_y-min_y):
        tot_dist = 0
        x_loc = i+min_x
        y_loc = j+min_y
        for k in range(len(coordinates)):
            distance = abs(coordinates[k][0]-x_loc)+abs(coordinates[k][1]-y_loc)
            tot_dist += distance
        if(tot_dist<10000):
            count+=1
#        column.append(tot_dist)
#    grid.append(column)

print(count)

