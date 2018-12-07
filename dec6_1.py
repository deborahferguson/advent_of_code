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

total_areas = [0]*len(coordinates)

grid = []
for i in range(max_x-min_x):
    column = []
    for j in range(max_y-min_y):
        min_distance = max_x-min_x+max_y-min_y
        min_distance_label = -1
        x_loc = i+min_x
        y_loc = j+min_y
        for k in range(len(coordinates)):
            distance = abs(coordinates[k][0]-x_loc)+abs(coordinates[k][1]-y_loc)
            if(distance<min_distance):
                min_distance = distance
                min_distance_label = k
        column.append(min_distance_label)
        total_areas[min_distance_label]+=1
    grid.append(column)

#negate any that are infinite
for i in [0,-1]:
    for j in range(max_y-min_y):
        total_areas[grid[i][j]]=0

for j in [0,-1]:
    for i in range(max_x-min_x):
        total_areas[grid[i][j]]=0

max_area = 0
for val in total_areas:
    if(val>max_area):
        max_area = val

print(max_area)



