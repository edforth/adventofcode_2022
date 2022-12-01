def part1(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    answer = str(lines)
    return answer

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    return answer


print("Part 1 answer = ", part1('day01input.txt'))
print("Part 2 answer = ", part2('day01input.txt'))
