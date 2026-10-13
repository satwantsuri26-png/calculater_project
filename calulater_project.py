import random
playing = True
number = str (random.randint(0,9))
fruit = ("apple")

print ("I will generate a number from 0 to 9 and a fruit; you have to guess it one didgit at a time!")
print ("The game ends when you guess the number and the fruit!")

while playing:
    guess = input("Give me your best guess for the number (only the number)! /n")
    if number == guess:
        print ("You win the game! You are now the hero of the number guessing game! Well done!")
        print ("The number was... ", number)
        break

    else:
        print ("Your guess isn't quite right! Try again! /n")

while playing:
    guess = input("Give me your best guess for the fruit (only the fruit with no punctuation and in all lowercase)! /n")
    if fruit == guess:
        print ("You win the game! You are now the hero of the fruit guessing game! Well done!")
        print ("The fruit was... ", fruit)
        break

    else:
        print ("Your guess isn't quite right! Try again! /n")
