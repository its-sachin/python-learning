import random
winner = random.randint(1,100)
guessed = int(input("Please guess any number between 1 to 100: "))
game = False
i = 1
while not game:
    if guessed == winner:
        print("You won")
        print(f"You took {i} chances to guess corectly")
        game = True
    elif guessed < winner:
            print("Man...its too low try something big.")
            guessed = int(input("Guess again: "))
            i += 1
    else:
            print("Man.. its too big try something small.")
            guessed = int(input("Guess again..."))
            i += 1






    


