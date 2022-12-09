#import numpy as np

def part1(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        input = f.read()
        #print(input)
    for i in range(0, len(input)-4):
        checkset = [
            input[i],
            input[i+1],
            input[i+2],
            input[i+3],
        ]
        if len(set(checkset)) == len(checkset):
            return i+4

    return False

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        input = f.read()
        #print(input)
    for i in range(0, len(input)-14):
        checkset = [
            input[i],
            input[i+1],
            input[i+2],
            input[i+3],
            input[i+4],
            input[i+5],
            input[i+6],
            input[i+7],
            input[i+8],
            input[i+9],
            input[i+10],
            input[i+11],
            input[i+12],
            input[i+13],
        ]
        if len(set(checkset)) == len(checkset):
            return i+14

    return False


print("Part 1 test answer = ", part1('day06input-testcase1.txt'))
print("Part 1 test answer 2 = ", part1('day06input-testcase2.txt'))
print("Part 1 answer = ", part1('day06input.txt'))
#Correct!!! (1262)
print("Part 2 test answer = ", part2('day06input-testcase1.txt'))
print("Part 2 test answer 2 = ", part2('day06input-testcase2.txt'))
print("Part 2 answer = ", part2('day06input.txt'))
#EASY!  (I'll probably pay for that hubris later)  (3444)
