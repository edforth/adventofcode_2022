def part1(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().split("\n\n")
    #print(lines)
    maxcalories = 0
    for line in lines:
        sackitems = line.split("\n")
        while("" in sackitems):
            sackitems.remove("")
        #print(sackitems)
        sackcalories = 0
        for sackitem in sackitems:
            sackitem = int(sackitem)
            sackcalories = sackcalories + sackitem
        if sackcalories > maxcalories:
            maxcalories = sackcalories 
    return str(maxcalories)

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().split("\n\n")
    elflist = []
    for line in lines: 
        print(line)
        sackitems = line.split("\n")
        while("" in sackitems):
            sackitems.remove("")
        sackcalories = 0
        print(sackitems)
        for sackitem in sackitems:
            sackitem = int(sackitem)
            sackcalories = sackcalories + sackitem
        elflist.append(sackcalories)
    elflist.sort()
    #print(elflist)
    answer = elflist[-1] + elflist[-2] + elflist[-3]
    return answer

print("Part 1 test case 1 answer = ", part1('day01input-testcase1.txt'))
print("Part 1 answer = ", part1('day01input.txt'))
#Correct on first attempt!   67016
print("Part 2 test case 1 answer = ", part2('day01input-testcase1.txt'))
print("Part 2 answer = ", part2('day01input.txt'))
#188382 Is wrong :(
#Got it right second try (200116).  I had forgot to update the read() in my template to split on double linebreak
