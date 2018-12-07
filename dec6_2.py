""" This solves the advent of code December 6 part 2"""

def read_data():
    """This function reads in the data and returns a list of coordinates
    as tuples, the x range, and the y range"""
    input_file = open("input_data/dec6.txt", 'r')
    coordinates = []
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    first = True
    for line in input_file:
        values = line.split(', ')
        x_value = int(values[0])
        y_value = int(values[1])
        coordinates.append((x_value, y_value))
        if first:
            min_x = x_value
            max_x = x_value
            min_y = y_value
            max_y = y_value
            first = False
        else:
            if x_value < min_x:
                min_x = x_value
            if x_value > max_x:
                max_x = x_value
            if y_value < min_y:
                min_y = y_value
            if y_value > max_y:
                max_y = y_value
    input_file.close()
    return coordinates, (min_x, max_y), (min_y, max_y)

def closest_region():
    """This function finds and returns the size of the region containing all locations
    with a total distance to all coordinates that is less than 10000 """
    coordinates, x_range, y_range = read_data()
    count = 0
    furthest_distance = int(10000/len(coordinates))
    for i in range(x_range[1]-x_range[0]+2*furthest_distance):
        for j in range(y_range[1]-y_range[0]+2*furthest_distance):
            tot_dist = 0
            x_loc = i+x_range[0]-furthest_distance
            y_loc = j+y_range[0]-furthest_distance
            for _, item in enumerate(coordinates):
                distance = abs(item[0]-x_loc)+abs(item[1]-y_loc)
                tot_dist += distance
            if tot_dist < 10000:
                count += 1
    return count

print(closest_region())
