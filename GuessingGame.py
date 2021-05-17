import random

guesses = []
my_list = random.randint(1, 100)

player = int(input("Enter a number between 1, 100: "))
guesses.append(player)

while player != my_list:
    if player > my_list:
        print("The number is too high!")
    else:
        print("The number is too low!")
    player = int(input("Enter a number between 1,100: "))
    guesses.append(player)

else:
    print("You have guessed right, Good job!")
    print(f"It took you {len(guesses)} guesses.")
    print("These are your guesses:")
    print(guesses)
