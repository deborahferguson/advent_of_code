"""This program solves the Advent of Code challenge for December 6 part 1"""

def read_data():
    """This function read in the data and returns the coordinates,
    the x range and the y range"""
    input_file = open("input_data/dec6.txt", 'r')
    coordinates = []
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    first = True
    for line in input_file:
        values = line.split(', ')
        x_val = int(values[0])
        y_val = int(values[1])
        coordinates.append((x_val, y_val))
        if first:
            min_x = x_val
            max_x = x_val
            min_y = y_val
            max_y = y_val
            first = False
        else:
            if x_val < min_x:
                min_x = x_val
            if x_val > max_x:
                max_x = x_val
            if y_val < min_y:
                min_y = y_val
            if y_val > max_y:
                max_y = y_val
    input_file.close()
    return coordinates, (min_x, max_x), (min_y, max_y)


def largest_finite_area():
    """This function finds and returns the largest finite
    area associated with a coordinate"""
    coordinates, x_range, y_range = read_data()

    total_areas = [0]*len(coordinates)

    grid = []
    for i in range(x_range[1]-x_range[0]):
        column = []
        for j in range(y_range[1]-y_range[0]):
            min_distance = x_range[1]-x_range[0]+y_range[1]-y_range[0]
            min_distance_label = -1
            for k, item in enumerate(coordinates):
                distance = abs(item[0]-i-x_range[0])+abs(item[1]-j-y_range[0])
                if distance < min_distance:
                    min_distance = distance
                    min_distance_label = k
            column.append(min_distance_label)
            total_areas[min_distance_label] += 1
        grid.append(column)


    for i in [0, -1]:
        for j in range(y_range[1]-y_range[0]):
            total_areas[grid[i][j]] = 0

    for j in [0, -1]:
        for i in range(x_range[1]-x_range[0]):
            total_areas[grid[i][j]] = 0

    max_area = 0
    for val in total_areas:
        if val > max_area:
            max_area = val

    return max_area

print(largest_finite_area())
