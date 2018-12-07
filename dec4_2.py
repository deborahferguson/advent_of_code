#Create list to store the data in
lines = []

#Read in the data
with open("input_data/dec4.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

#Sort the data
lines.sort()

#Create a dict storing the guard and a array of mintues_slept
guards = {}

curr_guard = 0#Current guard
awake = True#Current guard is awake?
fell_asleep_minute = 0#When did the current guard fall asleep?
for line in lines:
    if line[19] =='G':#If new guard
        #Do stuff for current guard
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
        if curr_guard in guards:
            curr_guard_minutes = guards[curr_guard]
            for i in range(fell_asleep_minute,awoke_minute):
                curr_guard_minutes[i]+=1
            guards[curr_guard] = curr_guard_minutes
        else:
            curr_guard_minutes = [0]*60
            for i in range(fell_asleep_minute,awoke_minute):
                curr_guard_minutes[i]+=1
            guards[curr_guard] = curr_guard_minutes
                

        awake = True
    
#Find which guard sleeps the most
max_sleep_minute = 0
max_sleep_count = 0
max_guard = 0
for guard,minutes in guards.items():
    for i in range(60):
        if(minutes[i]>max_sleep_count):
            max_sleep_minute = i
            max_sleep_count = minutes[i]
            max_guard = guard

print(max_guard*max_sleep_minute)
    

