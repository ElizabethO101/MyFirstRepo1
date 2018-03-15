import random

number = random.randint(0,3)

words = ["HAPPY","SWEETS","OCEAN","SPORTS"]
hint1 = ["A positive feeling","cupcakes","beach","game"]
hint2 = ["Name of song","baking","seagul","scoring"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess my secret word!")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input().upper()
    
    if guess == secretword:
        print("Yay! You guessed my word!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "HINT1":
        print(hint1[number])

    elif guess == "HINT2":
        print(hint2[number])

    elif guess == "FIRST LETTER":
        print(secretword[0])

    elif guess == "GIVE UP":
        print("You failed, it took you " + str(counter) + " many times.")
        print("My secret word was " + secretword)

    else:
        counter += 1
        print("Guess again!")
    
