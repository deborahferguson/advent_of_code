import string

def get_times():
    upper_case = string.ascii_uppercase
    times = {}
    for i,val in enumerate(upper_case):
        times[val] = 60+i+1
        #times[val] = i+1
    return times

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

def fill_time(workers,time,worker,step):
    for i in range(time):
        workers[worker].append(step)

def fill_down_time(workers):
    lengths = []
    for val in workers:
        lengths.append(len(val))
    lengths.sort()
    curr_short = 0
    curr_second = 1
    shortest = 0
    second_shortest = 0
    padding = 0
    while padding == 0 and curr_second<5:
        shortest = lengths[curr_short]
        second_shortest = lengths[curr_second]
        padding = second_shortest - shortest
        curr_short+=1
        curr_second+=1
    for val in workers:
        if(len(val)==shortest):
            for i in range(padding):
                val.append('')
        

def next_free_workers(workers):
    steps = []
    shortest_times = len(workers[0])
    free_workers = []
    for i,val in enumerate(workers):
        if(len(val)<shortest_times):
            shortest_times = len(val)
    for i,val in enumerate(workers):
        if(len(val)==shortest_times):
            free_workers.append(i)
            if(len(val)>0):
                steps.append(val[-1])
    return free_workers, steps

def get_total_time(workers):
    longest = 0
    for val in workers:
        if(len(val)>longest):
            longest = len(val)

    return longest


def print_len_each_worker(workers):
    for i,val in enumerate(workers):
        print(i,val)


def time_spent():
    step_times = get_times()
    
    tot_time = 0
    workers = []
    for i in range(5):
    #for i in range(2):
        time_array = []
        workers.append(time_array)

    #Read in the steps and their prereqs
    order_pairs = read_data()
    #Keep going until all the steps are done
    while True:
        #If all the steps are done
        if(len(order_pairs) == 0):
            break
        #Find the next free worker/finished task
        free_workers,finished_steps = next_free_workers(workers)
        for done_step in finished_steps:
            if(done_step!=""):
                #delete it as a prereq from remaining steps
                for key, value in order_pairs.items():
                    if done_step in value:
                        value.remove(done_step)
        
        #Find any available steps
        available_steps = []
        for key,value in order_pairs.items():
            if(len(value)==0):
                available_steps.append(key)
        available_steps.sort()
        
        if(len(available_steps)>0):
            #Assign the first step to a worker
            next_step = available_steps[0]
            fill_time(workers,step_times[next_step],free_workers[0],next_step)
            #remove it from the dictionary
            del order_pairs[next_step]
        else:
            fill_down_time(workers)

    return get_total_time(workers)

print(time_spent())

