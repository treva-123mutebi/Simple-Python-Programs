import random ##imports the random module

def getAnswer(answerNumber): ##getAnswer function is defined
    if answerNumber == 1:    ##r value stored in a parameter named answerNumber
        return 'So Close to Winning'
    elif answerNumber == 2:
        return 'It is a wrong guess'
    elif answerNumber == 3:
        return 'Three was already taken'
    elif answerNumber == 4:
        return 'You Have won 9 million usd'
    elif answerNumber == 5:
        return 'Try Again Never'
    elif answerNumber == 6:
        return 'So Not Close'
    elif answerNumber == 7:
        return 'No sorry'
    elif answerNumber == 8:
        return 'Wild guessing sorry'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1,9) ##evaluates to a random interger between 1 and 9
fortune = getAnswer(r) ##execution moves to the top of the getAnswer90
print(fortune)
