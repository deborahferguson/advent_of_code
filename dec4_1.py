#Create list to store the data in
lines = []

#Read in the data
#with open("../../Downloads/camDataDay4.txt") as f:
with open("input_data/dec4.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

#Sort the data
lines.sort()

#Create a dict storing the guard and a list of [total minutes asleep,[(fell_asleep,woke_up)]]
guards = {}

curr_guard = 0#Current guard
awake = True#Current guard is awake?
fell_asleep_minute = 0#When did the current guard fall asleep?
index = 0#Keep track of what line we're on
for line in lines:
    if line[19] =='G':#If new guard
        index_of_hash = line.find('#')
        index_end_number = line.find(' ',index_of_hash)
        guard_id = int(line[index_of_hash+1:index_end_number])
        curr_guard = guard_id
    elif awake:#If guard is falling asleep
        minute = int(line[15:17])
        fell_asleep_minute = minute
        awake = False
    else:#If guard is waking up
        awoke_minute = int(line[15:17])
        sleep_time = awoke_minute - fell_asleep_minute
        if curr_guard in guards:
            guards[curr_guard][0]+=sleep_time
            guards[curr_guard][1].append((fell_asleep_minute,awoke_minute))
        else:
            guards[curr_guard] = [sleep_time,[(fell_asleep_minute,awoke_minute)]]
        awake = True
    index +=1

#Find which guard sleeps the most
max_sleep = 0
max_guard = 0
for key,value in guards.items():
    sleep_min = value[0]
    if(sleep_min>max_sleep):
        max_sleep = sleep_min
        max_guard = key

#Create an array to represent the minutes. The value shows how many times the guard has been asleep during that minute
asleep_minutes = [0]*60
for nap in guards[max_guard][1]:
    for i in range(nap[0],nap[1]):
        asleep_minutes[i]+=1

#Find the minute he was asleep during most
max_sleep_minute = 0
max_sleep_times = 0
for i in range(len(asleep_minutes)):
    if(asleep_minutes[i]>max_sleep_times):
        max_sleep_times = asleep_minutes[i]
        max_sleep_minute = i

print(max_guard*max_sleep_minute)
    

