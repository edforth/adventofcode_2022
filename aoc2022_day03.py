def findMisfile(compartment1, compartment2):
    for char in compartment1:
        if char in compartment2:
            return char
    return False

def getPriority(char):
    if char == char.upper():
        return ord(char) - 38
    elif char == char.lower():
        return ord(char) - 96
    else:
        print("doesn't match upper or lower")
        return False

def findBadge(list):
    for char in list[0]:
        if char in list[1] and char in list[2]:
            return char
    return False 




def part1(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    prioritysum = 0 
    for line in lines:
        if len(line) % 2 == 0:
            length = int(len(line))
            half = int(len(line) / 2)
        else: 
            print("line has odd number of components")
            break
        compartment1 = line[0:half]
        compartment2 = line[half:length]
        misfile = findMisfile(compartment1, compartment2)
        if misfile:
            prioritysum = prioritysum + getPriority(misfile)
        else:
            print("no misfile???")
            return False

    return prioritysum

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()

    #create list of groups
    groups = []
    groupindex = 0
    while groupindex +2 <= len(lines):
        group = [
            lines[groupindex],
            lines[groupindex+1],
            lines[groupindex+2]
        ]
        groups.append(group)
        groupindex = groupindex + 3

    #basically the same as part one, but check everything in first set against both other sets, then get priority
    prioritysum = 0 
    for group in groups:
        badge = findBadge(group)
        if badge: 
            prioritysum = prioritysum + getPriority(badge)
        else:
            print("could not find badge :(")
            return False
    return prioritysum

#print("Part 1 test answer = ", part1('day03input-testcase1.txt'))
print("Part 1 answer = ", part1('day03input.txt'))
#First try!  7737
#print("Part 1 test answer = ", part2('day03input-testcase1.txt'))
print("Part 2 answer = ", part2('day03input.txt'))
#First try! 2697
