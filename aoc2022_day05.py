def moveCrates(numbermoved, startstack, endstack, stacks):
    for i in range(0, numbermoved): 
        cratecontents = stacks[startstack - 1].pop(0)
        stacks[endstack - 1].insert(0, cratecontents)
    return stacks 

def moveMultipleCrates(numbermoved, startstack, endstack, stacks):
    cratecontents = [] 
    for i in range(0, numbermoved): 
        cratecontents.insert(0, stacks[startstack - 1].pop(0))
    for crate in cratecontents:
        stacks[endstack - 1].insert(0, crate)
    return stacks 


def getStacks(drawing):
    #return getStacksTestCase1()
    return getStacksInputFile()

def getStacksTestCase1():
    stacks = [
        ['N', 'Z'],
        ['D', 'C', 'M'],
        ['P']
    ]
    return stacks

def getStacksInputFile():
    stacks = [
        ['Q', 'F', 'L', 'S', 'R'],
        ['T', 'P', 'G', 'Q', 'Z', 'N'],
        ['B', 'Q', 'M', 'S'],
        ['Q', 'B', 'C', 'H', 'J', 'Z', 'G', 'T'],
        ['S', 'F', 'N', 'B', 'M', 'H', 'P'],
        ['G', 'V', 'L', 'S', 'N', 'Q', 'C', 'P'],
        ['F', 'C', 'W'],
        ['M', 'P', 'V', 'W', 'Z', 'G', 'H', 'Q'],
        ['R', 'N', 'C', 'L', 'D', 'Z', 'G']
    ]
    return stacks 

def topCrates(stacks):
    output = ''
    for stack in stacks:
        output = output + stack[0]
    return output

def part1(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().split('\n\n')
    stacks = getStacks(lines[0])
    print(stacks)
    instructions = lines[1].splitlines()
    for instruction in instructions:
        split = instruction.split(' ')
        numbermoved = int(split[1])
        startstack = int(split[3])
        endstack = int(split[5])
        #print("move " + str(numbermoved) + " from " + str(startstack) + " to " + str(endstack))
        stacks = moveCrates(numbermoved, startstack, endstack, stacks)
        print(stacks)
    answer = topCrates(stacks)
    return answer

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().split('\n\n')
    stacks = getStacks(lines[0])
    print(stacks)
    instructions = lines[1].splitlines()
    for instruction in instructions:
        split = instruction.split(' ')
        numbermoved = int(split[1])
        startstack = int(split[3])
        endstack = int(split[5])
        #print("move " + str(numbermoved) + " from " + str(startstack) + " to " + str(endstack))
        stacks = moveMultipleCrates(numbermoved, startstack, endstack, stacks)
        print(stacks)
    answer = topCrates(stacks)
    return answer



#print("Part 1 test answer = ", part1('day05input-testcase1.txt'))
#print("Part 1 answer = ", part1('day05input.txt'))
#Test case worked.  First answer was incorrect (PGFQSGFMR)   I had forgotten to change the input file, so I was running the test case's instructions on the full input's stacks
# Running with correct instructions provided correct answer (FZCMJCRHZ)
#print("Part 2 test answer = ", part2('day05input-testcase1.txt'))
print("Part 2 answer = ", part2('day05input.txt'))
# First try!!  (JSDHQMZGF)
