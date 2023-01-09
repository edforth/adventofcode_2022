



def part1(inputfile):
    #Initial idea is to create a grid the same size a tree grid and use each sell to track if the tree is visible from a direction
    # so, I'll run four functions, "visible_from_left, visible_from_top, etc" and the for each cell in a row or column, 
    # check if a tree is visible against the highest height found so far, and stop once I hit a 9
    # that way I will hopefully not have to check any more trees than needed. 
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        if len(line) != len(lines[0]):
            print('ERROR: Irregular grid')
    xlength = len(lines[0])
    ylength = len(lines)
    print(str(xlength) + ", " + str(ylength)) 
    scoregrid = []
    for i in range(0, ylength):
        gridrow = []
        for i in range(0, xlength):
            gridrow.append(0)
        scoregrid.append(gridrow)
    print(scoregrid)
    return answer

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    return answer


print("Part 1 test answer = ", part1('day08input-testcase1.txt'))
print("Part 1 test answer 2 = ", part1('day08input-testcase2.txt'))
#print("Part 1 answer = ", part1('day08input.txt'))
#print("Part 2 test answer = ", part2('day08input-testcase1.txt'))
#print("Part 2 answer = ", part2('day08input.txt'))
