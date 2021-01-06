from random import randrange

# variables
win = 0
loss = 0
draw = 0
pval = ''
randchoice = ''


# function for starting the game
def start_game():
    while True:
        val = input("Want to play? (y = yes, n = no, r = win loss record): ").lower().strip()
        if val not in ['y', 'n', 'r']:
            print("Please enter valid input")
        elif val == 'y':
            player_value()
            computer_value()
            compare()
            start_game()
        elif val == 'r':
            record()
            start_game()
        elif val == 'n':
            print("Thanks for playing")
            break


# function for getting the player's choice
def player_value():
    global pval
    while True:
        pval = input("Choose Rock, Paper, or Scissors: ").lower().strip()
        if pval not in ['rock', 'paper', 'scissors']:
            print("Please enter valid input")
        else:
            break


# function for getting the computer's choice
def computer_value():
    global randchoice
    randchoice = randrange(0, 3)
    if randchoice == 0:
        compval = 'rock'
    elif randchoice == 1:
        compval = 'paper'
    else:
        compval = 'scissors'
    print(f"The computer chose {compval}")


# function for comparing the two
def compare():
    global win, loss, draw
    if pval == 'rock' and randchoice == 2 or \
            pval == 'paper' and randchoice == 0 or \
            pval == 'scissors' and randchoice == 1:
        win += 1
        print("you won")
    elif pval == 'rock' and randchoice == 0 or \
            pval == 'paper' and randchoice == 1 or \
            pval == 'scissors' and randchoice == 2:
        draw += 1
        print("it was a draw")
    else:
        loss += 1
        print("You lose")


# function for retrieving the win/loss record
def record():
    print(f"wins: {win}\nlosses: {loss}\ndraws: {draw}")


if __name__ == "__main__":
    start_game()
