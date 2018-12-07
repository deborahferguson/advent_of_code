f = open("input_data/dec5.txt")

polymer = ""
for line in f:
    polymer = line
f.close()

i=0
while(i<len(polymer)-1):
    curr_char = polymer[i]
    next_char = polymer[i+1]
    if(curr_char != next_char and (curr_char.lower()==next_char or curr_char==next_char.lower()) ):
        if(i+2<len(polymer)):
            polymer = polymer[0:i]+polymer[i+2:]
        else:
            polymer = polymer[0:i]
        i-=1
    else:
        i+=1

polymer = polymer.strip()
#print(polymer)
print(len(polymer))
