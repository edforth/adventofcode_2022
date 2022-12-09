debug = False  

def getElfPairs(lines):
    elfpairs = []
    for line in lines:
        assigments = line.split(",")
        #print(assigments)
        bounds = []
        for assigment_bound in assigments:
            numbers = assigment_bound.split("-")
            number_append = []
            for number in numbers:
                number_append.append(int(number))
            #print(number)
            bounds.append(number_append)
        elfpairs.append(bounds)
    return elfpairs

def isFullOverlap(pair):
    overlap = 0
    if pair[0][0] < pair[1][0]:
        if pair[0][1] >= pair[1][1]:
            overlap = 1
    elif pair[0][0] > pair[1][0]:
        if pair[0][1] <= pair[1][1]:
            overlap = 1
    elif pair[0][0] == pair[1][0]:
        overlap = 1
    else:
        print("Could not determine Overlap")
        return False 
    if debug:
        print("pair = " + str(pair))
        print("pair0 = " + str(pair[0]))
        print("pair1 = " + str(pair[1]))
        print("overlap = " + str(overlap))
    #print(debugout)

    return overlap


def isAnyOverlap(pair):
    overlap = 0
    if pair[0][0] < pair[1][0]:
        if pair[0][1] >= pair[1][0]:
            overlap = 1
    elif pair[0][0] > pair[1][0]:
        if pair[0][0] <= pair[1][1]:
            overlap = 1
    elif pair[0][0] == pair[1][0]:
        overlap = 1
    else:
        print("Could not determine Overlap")
        return False 

    return overlap

def part1(inputfile):
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    elfpairs = getElfPairs(lines)
    

    overlaps = 0
    for pair in elfpairs:
        overlap = isFullOverlap(pair)
        overlaps += overlap
    answer = overlaps 
    return answer

def part2(inputfile):
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    elfpairs = getElfPairs(lines)
    overlaps = 0
    for pair in elfpairs:
        overlap = isAnyOverlap(pair)
        overlaps += overlap
    answer = overlaps
    return answer

#print("Part 1 test answer = ", part1('day04input-testcase1.txt'))
#print("Part 1 test answer = ", part1('day04input-testcase2.txt'))
#print("Part 1 answer = ", part1('day04input.txt'))
#wrong answer, too high (567) Test case had worked "Curiously it's the right answer for someone else" Verified correct puzzle input
#it was 540.  I did not set the boundary numbers to integers, and was comparing them as strings. 
print("Part 2 test answer = ", part2('day04input-testcase1.txt'))
#print("Part 2 test answer = ", part2('day04input-testcase2.txt'))
print("Part 2 answer = ", part2('day04input.txt'))
