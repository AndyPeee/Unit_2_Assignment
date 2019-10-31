guessingdict = {(1, 1, 1): 1, (1, 1, 2): 1, (1, 2, 1): 1, (1, 2, 2,): 2, (2, 1, 1): 1, (2, 1, 2): 2, (2, 2, 1): 2, (2, 2, 2): 2}  # sets the dictionary with the tuples of possible recent answers as keys, and the computer guess as the value
total = 0
y = 0
a = 0  # sets the variables to be used later
b = 0
c = 0
first_three_counter = 1
points = 0
games = 0
computerpoints = 0
next_guess = 2
while True:  #starts the game
    recentguesses = (a, int(b), int(c))  # sets the tuple with vairables to be cycled through, and compared with the tuples in the dictionary. It is a tuple so that there is always 3 numbers in use
    if games == 9:  # ends the game so that there is a winner (odd number) and after a reasonable length (it gets boring)
        if computerpoints < points:  # selects winner based on how many computer guessed right
            winner = "you"
        else:
            winner = "you don't"
        exit(code="You have " + str(points)+" points, the computer has " + str(computerpoints)+" points, " + str(winner)+" win")  # ends game and displays winner and score (IN RED TEXT!!! how cool)
    elif first_three_counter <= 3:  # makes a loop that happens 3 times to guess 2 while setting up the previous guesses to be assesed
        a = int(b)  # moves the position of the guesses to the next spot in the tuple to make space for the next guess
        b = int(c)
        guess = int(input("guess "))  # takes the guess of the player
        print("the computer's guess was "+str(next_guess))  # prints the computers guess so the player knows they didn't cheat
        if guess == next_guess:  # compares guess vs estimated guess, gives points depended on the outcome
            computerpoints = computerpoints+1
        else:
            points = points+1
        print("computer points "+str(computerpoints))
        print("your points "+str(points))  # prints the points of both players
        next_guess = 2  # keeps the computer guessing 2 until there is enough data to be assesed
        first_three_counter = first_three_counter+1  # ends the loop when there is enough data to compare
        c = int(guess)  # adds the last guess to the tuple holding guesses
        games += 1
    else:  # this part of the if statement is for when there has been enough data to compare with the tuple
        guess = input("guess ")
        c = int(guess)
        next_guess = guessingdict[recentguesses]  # takes the tuple of previous player guesses and takes the value in the dictionary for this tuple and makes it the computers guess
        print("the computer's guess was " + str(next_guess))
        if int(guess) == int(next_guess):  # compares guesses and computer data, gives points to respective team
            computerpoints = computerpoints + 1
        else:
            points = points+1
        print("computer points " + str(computerpoints))
        print("your points " + str(points))
        a = int(b)  # moves the guesses to the next spot in the tuple to be read again into the dictionary
        b = int(c)
        games += 1  # increases the rounds played, meaning the game shortens by a round each round
