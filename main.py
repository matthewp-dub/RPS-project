from random import randrange

# assorted variables and the loop for restarting the game
win = 0
loss = 0
draw = 0
again = input('Want to play? Type "y" for yes or "n" for no: ') \
            .lower().strip()
while again not in ['y', 'n']:
    if again not in ['y', 'n']:
        print('Please enter a valid input')
    again = input('Want to play? Type "y" for yes or "n" for no: ').lower().strip()

while again != 'n':

    # the player's value, with some precautions against common errors
    val = input("Choose Rock, Paper, or Scissors: ").lower().strip()

    while val not in ['rock', 'paper', 'scissors']:
        print('Please enter a valid input')
        val = input("Choose Rock, Paper, or Scissors: ").lower().strip()

    # generates the random number and assigns a printable value
    # rock = 0, paper = 1, scissors = 2
    compval = ''
    randchoice = randrange(0, 3)
    if randchoice == 0:
        compval = 'rock'
    elif randchoice == 1:
        compval = 'paper'
    else:
        compval = 'scissors'
    print(f"The computer chose {compval}")

    # a check to decide who wins and who loses
    if val == 'rock' and randchoice == 2 or \
            val == 'paper' and randchoice == 0 or \
            val == 'scissors' and randchoice == 1:
        win += 1
        print("you won")
    elif val == 'rock' and randchoice == 0 or \
            val == 'paper' and randchoice == 1 or \
            val == 'scissors' and randchoice == 2:
        draw += 1
        print("it was a draw")
    else:
        loss += 1
        print("You Lose")

    again = input('Want to play again? (y = yes, n = no, r = win/loss record): ').lower().strip()
    while again not in ['y', 'n']:
        if again not in ['r', 'y', 'n']:
            print('Please enter a valid input')
        if again == 'r':
            print(f"wins: {win}\nlosses: {loss}\ndraws: {draw}")
        again = input('Want to play again? (y = yes, n = no, r = win loss record): ').lower().strip()

print("Thanks for playing!")