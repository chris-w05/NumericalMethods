import random

MAXGAMES = 10
playAgain = 'y'

#Statistics for later
playerChoices = []
computerChoices = []
numGames = 0

#Game structrue
validOptions = ['r', 'p', 's']
gameRules = {
    'r': {'r': 'd', 'p': 'c', 's': 'p'},
    'p': {'r': 'p', 'p': 'd', 's': 'c'},
    's': {'r': 'c', 'p': 'p', 's': 'd'}
}
results = []

print("starting game")

while playAgain == 'y' and numGames < MAXGAMES:
    #Take in user input
    userInput = ''
    while userInput not in validOptions:
        userInput = input("\nChoose rock paper or scissors (r/p/s)\n")
        if(userInput not in validOptions):
            print(f"{userInput} is not a valid option")

    #Computer responeand storing inputs
    computerResoponse =  validOptions[random.randint(0,2)]
    playerChoices.append(userInput)
    computerChoices.append(computerResoponse)
    
    #Find result, p for player, c for computer, d for draw
    result = gameRules[userInput][computerResoponse]
    if result == 'p':
        print("You win!")
        results.append('p') 
    elif result == 'c':
        print("You lose!")
        results.append('c')
    else:
        print("It's a draw!")
        results.append('d')  
    numGames += 1
    
    #See if user wants ot play again
    playAgain = input("Play again? (y/n)\n")
    if numGames >= MAXGAMES:
        print("Maximum number of games reached")

print("Exiting game")
playerWins = results.count('p')
computerWins = results.count('c')
draws = results.count('d')

#Total number of games
#Lots of copying and pasting nearly the same block of code
playerWinPercent = (playerWins / numGames) * 100 if numGames > 0 else 0
computerWinPercent = (computerWins / numGames) * 100 if numGames > 0 else 0
drawPercent = (draws / numGames) * 100 if numGames > 0 else 0

#Percentage of rock paper scissors
playerRockPercent = (playerChoices.count('r')/numGames) * 100 if numGames > 0 else 0
playerPaperPercent = (playerChoices.count('p')/numGames) * 100 if numGames > 0 else 0
playerScissorsPercent = (playerChoices.count('s')/numGames) * 100 if numGames > 0 else 0

computerRockPercent = (computerChoices.count('r')/numGames) * 100 if numGames > 0 else 0
computerPaperPercent = (computerChoices.count('p')/numGames) * 100 if numGames > 0 else 0
computerScissorsPercent = (computerChoices.count('s')/numGames) * 100 if numGames > 0 else 0

print("\nGame Statistics:")
print(f"Total games played: {numGames}")
print(f"Player wins: {playerWins} ({playerWinPercent:.2f}%)")
print(f"Computer wins: {computerWins} ({computerWinPercent:.2f}%)")
print(f"Draws: {draws} ({drawPercent:.2f}%)")

print("\nPlayer choice distribution:")
print(f"Rock: {playerRockPercent:.2f}%, Paper: {playerPaperPercent:.2f}%, Scissors: {playerScissorsPercent:.2f}%")

print("\nComputer choice distribution:")
print(f"Rock: {computerRockPercent:.2f}%, Paper: {computerPaperPercent:.2f}%, Scissors: {computerScissorsPercent:.2f}%")
