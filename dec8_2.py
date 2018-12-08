def sum_metadata(tree):
    if(len(tree)==0):
        return 0,0
    
    num_children = tree[0]
    num_metadata = tree[1]

    if(num_children == 0):
        metadata_sum = 0
        for i in range(2,2+num_metadata):
            metadata_sum+=tree[i]
        length = 2+num_metadata
        value = metadata_sum
        return value, length

    child_values = []
    start_point = 2
    for i in range(num_children):
        sub_total, length = sum_metadata(tree[start_point:])
        start_point+=length
        child_values.append(sub_total)
    total = 0
    for i in range(start_point,start_point+num_metadata):
        curr_index = tree[i]-1
        if curr_index < len(child_values):
            total+=child_values[curr_index]

    return total, start_point+num_metadata

def sum_of_metadata():
    total_metadata = 0
    f = open("input_data/dec8.txt",'r')
    tree = []
    for line in f:
        line = line.strip()
        tree = [int(x) for x in line.split()]
    total_metadata = sum_metadata(tree)
    return total_metadata

print(sum_of_metadata()[0])
