filename = "input_data/dec2.txt"

#Set initial counts to 0
twos = 0
threes = 0

#open file
f = open(filename)
#For each id
for line in f:
    #Initially assume they have no doubles or tripples
    has_double = False
    has_triple = False
    letters = {}
    #Iterate through each character
    for char in line:
        #Add to the dictionary
        if char in letters:
            letters[char] = letters[char]+1
        else:
            letters[char] = 1
    #Search for doubles and triples in the dictionary
    for key, value in letters.items():
        if(value==2):
            has_double = True
        if(value==3):
            has_triple = True
        #Break if both are true already
        if(has_double and has_triple):
            break
    #Update the number of doubles and triples
    if(has_double):
        twos+=1
    if(has_triple):
        threes+=1

#Print the solution
print(twos*threes)
