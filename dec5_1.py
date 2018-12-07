filename = "input_data/dec5.txt"

f = open(filename)

polymer = ""
for line in f:
    polymer = line
f.close()

finished = False
len_poly = len(polymer)

while not finished:
    changed = False
    i = 0
    while i < len_poly-1:
        print(i,len_poly)
        curr_char = polymer[i]
        next_char = polymer[i+1]
        if(curr_char != next_char and (curr_char.lower()==next_char or curr_char == next_char.lower()) ):
            polymer = polymer[0:i]+polymer[i+2:]
            changed = True
            len_poly -=2
            i = i-1
        i=i+1
    if not changed:
        finished = True

polymer = polymer.strip()
print(polymer)
print(len(polymer))
