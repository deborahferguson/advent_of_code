
def read_data():
    order_pairs = {}
    #filename = "test_input.txt"
    filename = "input_data/dec7.txt"
    input_file = open(filename,'r')
    for line in input_file:
        first = line[5]
        second = line[36]
        if second in order_pairs:
            order_pairs[second].append(first)
        else:
            order_pairs[second] = []
            order_pairs[second].append(first)
        if first not in order_pairs:
            order_pairs[first] = []
    return order_pairs

def order_instructions():
    solution_order = ""
    
    order_pairs = read_data()
    while True:
        if(len(order_pairs) == 0):
            break
        available_steps = []
        for key,value in order_pairs.items():
            if(len(value)==0):
                available_steps.append(key)
        available_steps.sort()
        step = available_steps[0]
        solution_order = solution_order+step
        del order_pairs[step]
        for key, value in order_pairs.items():
            if step in value:
                value.remove(step)
        
    return solution_order
           
print(order_instructions())
