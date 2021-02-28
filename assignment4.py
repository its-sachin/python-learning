winner = 5
guess = int(input("Guess any number between 1 to 10 : "))
if guess == winner:
    print("Great you are a success sufferer")
else:
    if guess >= winner:
        print("Man...its too big, try something small")
    if guess<= winner:
        print("Man...its too small, try something big")

