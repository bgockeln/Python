#Rock Paper Scissors Game
import random
gameLoop = 0
playerScore = 0
computerScore = 0

#Choice function for Player
def playerCh():
    global playChVar
    playCh = input("Enter Rock, Paper or Scissor: ")
    if playCh == "Rock" or "rock":
        print("Player picked rock")
        playChVar = 1
    elif playCh == "Paper" or "paper":
        print("Player picked Paper")
        playChVar = 2
    elif playCh == "Scissor" or "scissor":
        print("Player picked Scissor")
        playChVar = 3
    elif playCh != "Rock" or "Paper" or "Scissor" or "rock" or "paper" or "scissor":
        print("Kaka")
        round()

#Choice function for Computer
def computerCh():
    global computerChVar
    num = random.randint(1, 3)
    if num == 1:
        print("Computer picked Rock")
        computerChVar = 1
    elif num == 2:
        print("Computer picked Paper")
        computerChVar = 2
    elif num == 3:
        print("Computer picked Scissor")
        computerChVar = 3

#Game Logic to play a single round
def round():
    global playerScore
    global computerScore
    playerCh()
    computerCh()
    if computerChVar == 1 and playChVar == 1:
        print("Tie, No Points")
    elif computerChVar == 1 and playChVar == 2:
        print("Paper beats Rock, point for the Player")
        playerScore += 1
    elif computerChVar == 1 and playChVar == 3:
        print("Rock beats Scissor, point for the Computer")
        computerScore += 1
    elif computerChVar == 2 and playChVar == 1:
        print("Paper beats Rock, Point for Computer")
        computerScore += 1
    elif computerChVar == 2 and playChVar == 2:
        print("Tie, no points")
    elif computerChVar == 2 and playChVar == 3:
        print("Scissor beats Paper, point for Player")
        playerScore += 1
    elif computerChVar == 3 and playChVar == 1:
        print("Rock beats Scissor, point for Player")
        playerScore += 1
    elif computerChVar == 3 and playChVar == 2:
        print("Scissor beats Paper, Point for Computer")
        computerScore += 1
    elif computerChVar == 3 and playChVar == 3:
        print("Tie")

print("""
Rock, Paper, Sissors Game.
Play a game of Rock, Paper, Scissors against the Computer.")
Whoever gets 3 points first, wins. 
    """)
while gameLoop == 0:
    round()
    print("Player has: ", playerScore, " Points. Computer has: ", computerScore, " Points.")
    if playerScore == 3:
        print("Player won")
        input("Press Enter to Quit")
        gameLoop = 1
    elif computerScore == 3:
        print("Computer won")
        input("Press Enter to Quit")
        gameLoop = 1

