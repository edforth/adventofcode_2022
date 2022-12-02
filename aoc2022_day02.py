def part1(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    myscore = 0
    for line in lines:
        choices = line.split(" ")
        if choices[0] == "A":
            theirchoice = "Rock"
        elif choices[0] == "B":
            theirchoice = "Paper"
        elif choices[0] == "C":
            theirchoice = "Scissors"
        if choices[1] == "X":
            mychoice = "Rock"
        elif choices[1] == "Y":
            mychoice = "Paper"
        elif choices[1] == "Z":
            mychoice = "Scissors"

        
        if mychoice == "Rock":
            shapescore = 1
        elif mychoice == "Paper":
            shapescore = 2
        elif mychoice == "Scissors":
            shapescore = 3
        else:
            return "jdhsklafhjdkhfaljkds"

        if theirchoice == mychoice:
            roundscore = 3
        elif theirchoice == "Rock" and mychoice == "Paper":
            roundscore = 6
        elif theirchoice == "Rock" and mychoice == "Scissors":
            roundscore = 0
        elif theirchoice == "Paper" and mychoice == "Rock":
            roundscore = 0
        elif theirchoice == "Paper" and mychoice == "Scissors":
            roundscore = 6
        elif theirchoice == "Scissors" and mychoice == "Rock":
            roundscore = 6
        elif theirchoice == "Scissors" and mychoice == "Paper":
            roundscore = 0
        else: 
            return "AUUUUUUGH!!!!!!!!!!"
        myscore = myscore + shapescore + roundscore

        #print(choices)
        #print("theirchoice = " + choices[0] + " = " + theirchoice  + ", " + "mychoice = " + choices[1] + " = " + mychoice)
        #print("shapescore = " + str(shapescore))
        #print("roundscore = " + str(roundscore))
        #print("myscore = " + str(myscore))

    answer = myscore
    return answer

def part2(inputfile):
    answer = ''
    with open(inputfile,'r') as f:
        lines = f.read().splitlines()
    myscore = 0
    for line in lines: 
        choices = line.split(" ")
        if choices[0] == "A":
            theirchoice = "Rock"
        elif choices[0] == "B":
            theirchoice = "Paper"
        elif choices[0] == "C":
            theirchoice = "Scissors"
        if choices[1] == "X":
            neededresult = "Lose"
            roundscore = 0
        elif choices[1] == "Y":
            neededresult = "Draw"
            roundscore = 3
        elif choices[1] == "Z":
            neededresult = "Win"        
            roundscore = 6
        if theirchoice == "Rock" and neededresult == "Lose":
            neededshape = "Scissors"
        elif theirchoice == "Rock" and neededresult == "Draw":
            neededshape = "Rock"
        elif theirchoice == "Rock" and neededresult == "Win":
            neededshape = "Paper"
        elif theirchoice == "Paper" and neededresult == "Lose":
            neededshape = "Rock"
        elif theirchoice == "Paper" and neededresult == "Draw":
            neededshape = "Paper"
        elif theirchoice == "Paper" and neededresult == "Win":
            neededshape = "Scissors"
        elif theirchoice == "Scissors" and neededresult == "Lose":
            neededshape = "Paper"
        elif theirchoice == "Scissors" and neededresult == "Draw":
            neededshape = "Scissors"
        elif theirchoice == "Scissors" and neededresult == "Win":
            neededshape = "Rock"
        else:
            return "failed to determin needed result"
        if neededshape == "Rock":
            shapescore = 1
        elif neededshape == "Paper":
            shapescore = 2
        elif neededshape == "Scissors":
            shapescore = 3
        else:
            return "Failed to convert shapescore"
        myscore = myscore + shapescore + roundscore
    answer = myscore
    return answer


#print("Part 1 test answer = ", part1('day02input-testcase1.txt'))
#print("Part 1 answer = ", part1('day02input.txt'))
#test case worked, but first answer on full didn't (13340)
#I confused theirchoice and mychoice and scored wins as losses and vice-versa.  Correct second time (11666)

print("Part 2 test answer = ", part2('day02input-testcase1.txt'))
print("Part 2 answer = ", part2('day02input.txt'))
#Got it first try (12767)

