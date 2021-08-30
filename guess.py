import random
print("number guessing game")
number = random.randint(1,9)
chances = 0
while chances<5:
    guess = int(input("enter your guess"))
    if guess==number:
        print("congrats you won")
        break
    elif guess<number:
        print("guess is too low, guess a higher number")
    else:
        print("guess is too high, guess a lower number")

    chances=chances+1

if not chances<5:
    print("you loose, the number is",number)
