#filename = "input_data/dec5.txt"
filename = "../../Downloads/day5.txt"

f = open(filename)

polymer = ""
for line in f:
    polymer = line
f.close()

best_length = len(polymer)

for pair in [('A','a'),('B','b'),('C','c'),('D','d'),('E','e'),('F','f'),('G','g'),('H','h'),('I','i'),('J','j'),('K','k'),('L','l'),('M','m'),('N','n'),('O','o'),('P','p'),('Q','q'),('R','r'),('S','s'),('T','t'),('U','u'),('V','v'),('W','w'),('X','x'),('Y','y'),('Z','z')]:
    new_polymer= polymer.replace(pair[0],"")
    new_polymer= new_polymer.replace(pair[1],"")

    print(pair)

    finished = False
    len_poly = len(new_polymer)
    
    while not finished:
        changed = False
        i = 0
        while i < len_poly-1:
            curr_char = new_polymer[i]
            next_char = new_polymer[i+1]
            if(curr_char != next_char and (curr_char.lower()==next_char or curr_char == next_char.lower()) ):
                new_polymer = new_polymer[0:i]+new_polymer[i+2:]
                changed = True
                len_poly -=2
                i = i-1
            i=i+1
        if not changed:
            finished = True

    new_polymer = new_polymer.strip()
    if(len(new_polymer)<best_length):
        best_length = len(new_polymer)

print(best_length)
